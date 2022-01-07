import sys
import logging
import time
import os
import math
from datetime import datetime

from PySide2.QtCore import QSize, Qt, QRunnable, QThreadPool, Signal, Slot, QEvent, QUrl
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel
from PySide2.QtCore import QUrl
from PySide2.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
import pyqtgraph as pg
from pyqtgraph import PlotWidget, plot

from drawablewidget import DrawableWidget

import qdarkstyle

from badbot_protos_pysrc import consts_pb2

from mainwindow import Ui_MainWindow
import messaging
import graphics_signals
import graphics_workers

from gamepad import GamepadStreamer
from gamepad_signals import GamepadStreamSignals

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        self.setWindowTitle("BadBot: Command and Control")

        # app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyside2'))

        # setup defaults
        self.operationalMode = consts_pb2.OperationalMode.IDLE


        self._vw = DrawableWidget()
        self.verticalLayout_4.addWidget(self._vw)


        #setup button handlers
        self.btn_enable_lidar_recording.clicked.connect(self.onBtnEnableLidarRecording)
        self.btn_disable_lidar_recording.clicked.connect(self.onBtnDisableLidarRecording)
        
        self.btn_enable_app_video.clicked.connect(self.onBtnEnableAppVideo)
        self.btn_disable_app_video.clicked.connect(self.onBtnDisableAppVideo)


        #setup control mode combo box values
        self.dd_operational_mode.addItems([
            consts_pb2.OperationalMode.Name(consts_pb2.IDLE),
            consts_pb2.OperationalMode.Name(consts_pb2.TELEOP),
            consts_pb2.OperationalMode.Name(consts_pb2.FOLLOW_ME),
            consts_pb2.OperationalMode.Name(consts_pb2.AUTONOMOUS)
        ])
        self.dd_operational_mode.currentIndexChanged.connect(self.onOperationalModeChanged)

        ###################
        ###################
        ###  set up video streams
        ###################
        ###################
        self.dd_stream.addItems([
            "Please select....",
            "Test Stream",
            "Live Stream"
        ])
        self.dd_stream.currentIndexChanged.connect(self.onVideoStreamChanged)

        self.btn_play.clicked.connect(self.onStartVideo)
        self.btn_stop.clicked.connect(self.onStopVideo)


        ###################
        ###################
        ###  set up status graph
        ###################
        ###################
        # self.systemGraph = pg.PlotWidget()
        # self.verticalLayout_9.addWidget(self.systemGraph)


        ###################
        ###################
        ###  set up status bar
        ###################
        ###################
        self.lbl_status_lidar = QLabel(self.statusbar)
        self.lbl_status_lidar.setText("LIDAR")

        self.lbl_status_gps = QLabel(self.statusbar)
        self.lbl_status_gps.setText("GPS")

        self.lbl_status_imu = QLabel(self.statusbar)
        self.lbl_status_imu.setText("IMU")

        self.lbl_status_app_video = QLabel(self.statusbar)
        self.lbl_status_app_video.setText("BOTCAM")

        self.lbl_motor_ctrl = QLabel(self.statusbar)
        self.lbl_motor_ctrl.setText("MOTCTRL")

        self.statusbar.addPermanentWidget(self.lbl_status_lidar)
        self.statusbar.addPermanentWidget(self.lbl_status_gps)
        self.statusbar.addPermanentWidget(self.lbl_status_imu)
        self.statusbar.addPermanentWidget(self.lbl_status_app_video)
        self.statusbar.addPermanentWidget(self.lbl_motor_ctrl)

        
        #load the horizon
        self.headingViewLoaded = False
        self.headingView = QWebEngineView()
        self.headingView.loadFinished.connect(self.onHeadingViewLoadFinished)

        path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "html-content-gauges/dash.html")
        self.headingView.load(QUrl.fromLocalFile(path))
        self.wd_horizon_attitude_layout = QVBoxLayout(self.wd_horizon_attitude)
        self.wd_horizon_attitude_layout.addWidget(self.headingView)

        #load the map
        self.mapViewLoaded = False
        self.mapView = QWebEngineView()
        self.mapView.loadFinished.connect(self.onMapViewLoadFinished)

        path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "html-content-map/index.html")
        self.mapView.load(QUrl.fromLocalFile(path))
        self.verticalLayout_8.addWidget(self.mapView)

        self.threadpool = QThreadPool()
        print("Thread pool size: [{}]".format(self.threadpool.maxThreadCount()))

        self.installEventFilter(self)

        #start the graphics generator process
        self.graphicsWorker = graphics_workers.GraphicsWorkers()
        self.graphicsWorker.signals.onLidarImageReady.connect(self.onLidarImageReady)
        self.graphicsWorker.signals.onDrivelineImageReady.connect(self.onDrivelineImageReady)
        self.threadpool.start(self.graphicsWorker)

        #start the gamepad listener
        self.gamepadStream = GamepadStreamer(self.threadpool)
        self.gamepadStream.signals.onStream.connect(self.onGamepadStream)
        #todo - uncomment the following lines to use gamepad
        if os.path.exists("/dev/input/js0"):
            self.gamepadStream.setup()
            self.threadpool.start(self.gamepadStream)
        else:
            logging.warning("Joystick unavailable")

        #start comms
        self.startMessagingService()

    def eventFilter(self, obj, event):

        if obj is self and event.type() == QEvent.Close:
            self.graphicsWorker.keep_running = False
            self.messagingServiceThread.keep_running = False
            self.gamepadStream.keep_running = False
            
        return super().eventFilter(obj, event)
    
    def startMessagingService(self):
        
        self.messagingServiceThread = messaging.BadBotMessagingService()

        self.messagingServiceThread.signals.onError.connect(self.onMessagingError)
        self.messagingServiceThread.signals.onBotStatus.connect(self.onBotStatus)
        self.messagingServiceThread.signals.onLidarScan.connect(self.onLidarData)
        self.messagingServiceThread.signals.onIMUData.connect(self.onIMUData)
        self.messagingServiceThread.signals.onGPSData.connect(self.onGPSData)
        self.messagingServiceThread.signals.onObjDetCoords.connect(self.onObjDetCoords)
        self.messagingServiceThread.signals.onDrivelineStatus.connect(self.onDrivelineStatus)

        self.threadpool.start(self.messagingServiceThread)

    @Slot()
    def onDrivelineStatus(self, status):
        self.graphicsWorker.enqueueDrivelineStatusForProcessing(status)
        

    @Slot()
    def onObjDetCoords(self, coords):
        
        coordsToDraw = None

        self._vw.updateRoiKfEstimate(coords.object_at_angle)

        for i in range(0, len(coords.coordinates)):
            if coords.coordinates[i].objId == 0:
                coordsToDraw = coords.coordinates[i]
                break
            
        if coordsToDraw is not None:
            
            # translated_x = (coordsToDraw.x/640) * 640
            # translated_y = (coordsToDraw.y/480) * 720
            # print(coordsToDraw, translated_x, translated_y)

            # self._vw.updateRect(translated_y, translated_x, coordsToDraw.h, coordsToDraw.w)
            print(coordsToDraw)
            self._vw.updateRect(coordsToDraw.y, coordsToDraw.x, coordsToDraw.h, coordsToDraw.w)
            self.graphicsWorker._person_at_angle = coords.object_at_angle

    @Slot()
    def onGamepadStream(self, vY, vX):
        if self.operationalMode is consts_pb2.OperationalMode.TELEOP:
            self.messagingServiceThread.sendVelCmd(vY, vX)
            #print("On Y:X", vY, vX)
    
    @Slot()
    def onMessagingError(self, err):
        print("Messaging error: " + err)

        #wait for 5 secs
        time.sleep(5)
        
        #start grpc comms
        self.startMessagingService()        
    
    def setSensorStatus(self, sensorLabel, statusGood):
        if statusGood:
            sensorLabel.setStyleSheet("QLabel { background-color : green; color: white; padding: 5px;}")
        else:
            sensorLabel.setStyleSheet("QLabel { background-color : red; color: white; padding: 5px;}")

    @Slot()
    def onBotStatus(self, status):
        
        self.lbl_status_lidar_recording.setText("{}".format(status.lidarRecordingEnabled))
        
        self.setSensorStatus(self.lbl_status_imu,status.imuHealthy)
        self.setSensorStatus(self.lbl_status_gps,status.gpsHealthy)
        self.setSensorStatus(self.lbl_status_lidar,status.lidarEnabled)
        self.setSensorStatus(self.lbl_status_app_video,status.appSrcEnabled)
        self.setSensorStatus(self.lbl_motor_ctrl, status.motorControllerHealthy)

        self.lbl_status_operational_mode.setText("{}".format(consts_pb2.OperationalMode.Name(status.mode)))
        self.lbl_status_last_updated.setText("{}".format(datetime.now()))
        self.lbl_status_cpu_load.setText("[{:.2f} / {:.2f} / {:.2f}] of [{}] cores".format(
            status.sysLoadAvg.oneMin, 
            status.sysLoadAvg.fiveMin, 
            status.sysLoadAvg.fifteenMin,
            status.sysLoadAvg.numCores
        ))
        self.lbl_status_memory.setText("[{:.0f}/{:.0f}]M [{:.0f}/{:.0f}]M".format(
            status.sysLoadAvg.freeRam / 1000000,
            status.sysLoadAvg.totalRam / 1000000,
            status.sysLoadAvg.freeSwap / 1000000,
            status.sysLoadAvg.totalSwap / 1000000
        ))


    @Slot()
    def onBtnEnableLidarRecording(self):
        self.messagingServiceThread.enableLidarRecording()
    
    @Slot()
    def onBtnDisableLidarRecording(self):
        self.messagingServiceThread.disableLidarRecording()
    
    @Slot()
    def onOperationalModeChanged(self, index):
        self.operationalMode = consts_pb2.OperationalMode.Value(self.dd_operational_mode.itemText(index))
        self.messagingServiceThread.setOperationalMode(self.operationalMode)
    
    @Slot()
    def onVideoStreamChanged(self, index):
        #0 is selection prompt
        #1 is test
        #2 is live

        media_url = "gst-pipeline: rtspsrc location=rtsp://10.42.0.1:8554/{} latency=0 ! rtph264depay ! avdec_h264 ! videoconvert ! autovideosink name=qtvideosink"
        #media_url = "gst-pipeline: rtspsrc location=rtsp://127.0.0.1:8554/{} latency=0 ! rtph264depay ! avdec_h264 ! videoconvert ! autovideosink name=qtvideosink"

        if index == 0:
            pass
        elif index == 1:
            self._vw.playVideo(media_url.format("test"))
        elif index == 2:
            self._vw.playVideo(media_url.format("hd"))
        else:
            print("Unknown media requested")
    
    @Slot()
    def onStopVideo(self):
        self._vw.stopVideo()

    @Slot()
    def onStartVideo(self):
        self._vw.startVideo()

    @Slot()
    def onBtnEnableAppVideo(self):
        self.messagingServiceThread.toggleAppVideo(True)
    
    @Slot()
    def onBtnDisableAppVideo(self):
        self.messagingServiceThread.toggleAppVideo(False)
    
    @Slot()
    def onBtnOpenAppVideo(self):
        pass

    @Slot()
    def onLidarData(self, lidarScan, ispoi):
        self.graphicsWorker.enqueueLidarScanForProcessing(lidarScan, ispoi)

    @Slot()
    def onIMUData(self, imuData):
        print(imuData)
        if self.headingViewLoaded == True:
            self.headingView.page().runJavaScript(
                "setState({:.2f},{:.2f},{:.2f})".format(
                    imuData.orientation.x,
                    imuData.orientation.y,
                    imuData.orientation.z
                )
            )
        
        self.lbl_status_pressure.setText("{:.2f}".format(imuData.pressure))
        self.lbl_status_altitude.setText("{:.2f} ft".format(imuData.altitude))
        self.lbl_status_temperature.setText("{:.2f} C".format(imuData.temperature))
    
    @Slot()
    def onGPSData(self, gpsData):
        print(gpsData)
        self.lbl_status_lat.setText("{}".format(gpsData.latitude))
        self.lbl_status_lon.setText("{}".format(gpsData.longitude))
        self.lbl_status_hdop.setText("{}".format(gpsData.hdop))
        self.lbl_status_vdop.setText("{}".format(gpsData.vdop))
        self.lbl_status_pdop.setText("{}".format(gpsData.pdop))
        self.lbl_status_sat_visible.setText("{}".format(gpsData.satellites_visible))
        self.lbl_status_sat_used.setText("{}".format(gpsData.satellites_used))

        # update map
        if self.mapViewLoaded:
            self.mapView.page().runJavaScript(
                "moveBotTo({},{})".format(
                    gpsData.latitude,
                    gpsData.longitude
                )
            )
        
    @Slot()
    def onHeadingViewLoadFinished(self):
        print("Heading view loaded")
        self.headingViewLoaded = True
    
    @Slot()
    def onMapViewLoadFinished(self):
        print("Map view loaded")
        self.mapViewLoaded = True
        
    @Slot()
    def onLidarImageReady(self, pixmap):
        self.lbl_lidar_map.clear()
        self.lbl_lidar_map.setPixmap(pixmap)
    
    @Slot()
    def onDrivelineImageReady(self, pixmap):
        # self.lbl_lidar_map.clear()
        # self.lbl_lidar_map.setPixmap(pixmap)
        self._vw.updateDriveline(pixmap)

logging.basicConfig()

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()