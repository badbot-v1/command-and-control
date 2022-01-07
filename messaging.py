import grpc
import messaging_signals
import time
import logging

from PySide2.QtCore import QRunnable, Signal, Slot

from google.protobuf import empty_pb2
from badbot_protos_pysrc import consts_pb2, message_pb2
from badbot_protos_pysrc import message_pb2
from badbot_protos_pysrc import cmdtoggle_pb2
from badbot_protos_pysrc import services_pb2_grpc

import zmq

context = zmq.Context()

class BadBotMessagingService(QRunnable):
    def __init__(self):
        super().__init__()
        self.keep_running = True
        self.signals = messaging_signals.MessagingSignals()
        self.sock_rx = context.socket(zmq.SUB)
        self.sock_tx = context.socket(zmq.PUB)

    def bm_create_toggle_message(self, device, enabled):
        msg = message_pb2.BadMessage()
        msg.msgType = consts_pb2.CMD_TOGGLE
        msg.toggleCmd.device = device
        msg.toggleCmd.enable = enabled

        return msg

    def bm_cmd_telemetry(self, enabled):

        return self.bm_create_toggle_message(consts_pb2.TELEMETRY, enabled).SerializeToString()

    def bm_cmd_lidar_recording(self, enabled):

        return self.bm_create_toggle_message(consts_pb2.LIDAR_RECORD, enabled).SerializeToString()
    
    def bm_cmd_app_video(self, enabled):

        return self.bm_create_toggle_message(consts_pb2.APPSRC, enabled).SerializeToString()

    def enableLidarRecording(self):

        try:
            self.txMessage(self.bm_cmd_lidar_recording(True))
        except:
            print("An exception occurred.")

    def disableLidarRecording(self):
        try:
            self.txMessage(self.bm_cmd_lidar_recording(False))
        except:
            print("An exception occurred.")

    def toggleAppVideo(self, enabled):
        try:
            self.txMessage(self.bm_cmd_app_video(enabled))
        except:
            print("An exception occurred.")
    
    def sendVelCmd(self, vY, vX):
        msg = message_pb2.BadMessage()
        msg.msgType = consts_pb2.CMD_TELEOP_MOVEMENT
        msg.cmdVel.vX = vX
        msg.cmdVel.vY = vY

        try:
            self.txMessage(msg.SerializeToString())
        except:
            print("An exception occurred.")

    def setOperationalMode(self, opMode):
        msg = message_pb2.BadMessage()
        msg.msgType = consts_pb2.CMD_OPERATIONAL_MODE
        msg.opMode.opMode = opMode

        try:
            self.txMessage(msg.SerializeToString())
        except:
            print("An exception occurred.")

    def txMessage(self, msg):
        self.sock_tx.send(msg)

    @Slot()
    def run(self):
        
        logging.log(logging.DEBUG, "Connecting to channel")

        try:
            # self.sock_tx.connect("tcp://127.0.0.1:40000")
            # self.sock_rx.connect("tcp://127.0.0.1:41000")

            self.sock_tx.connect("tcp://10.42.0.1:40000")
            self.sock_rx.connect("tcp://10.42.0.1:41000")

            #subscribe to all topics
            self.sock_rx.subscribe("")

            time.sleep(1.0)
    
            print("Enabling telemetry")
            self.txMessage(self.bm_cmd_telemetry(True))

            print("Connected, waiting for updates")

            while True:
                msg = self.sock_rx.recv()

                try:
                    

                    badmessage = message_pb2.BadMessage()
                    badmessage.ParseFromString(msg)


                    if self.keep_running == False:
                        break

                    if badmessage.msgType == consts_pb2.MessageType.STATUS_BOT:
                        self.signals.onBotStatus.emit(badmessage.status)

                    elif badmessage.msgType == consts_pb2.MessageType.TELE_IMU:
                        self.signals.onIMUData.emit(badmessage.imuData)

                    elif badmessage.msgType == consts_pb2.MessageType.TELE_GPS:
                        self.signals.onGPSData.emit(badmessage.gpsData)

                    elif badmessage.msgType == consts_pb2.MessageType.TELE_LIDAR:
                        self.signals.onLidarScan.emit(badmessage.lidarScan, False)

                    elif badmessage.msgType == consts_pb2.MessageType.TELE_LIDAR_POI:
                        self.signals.onLidarScan.emit(badmessage.lidarScan, True)
                    
                    elif badmessage.msgType == consts_pb2.MessageType.VPM_OBJ_DET_COORDS:
                        self.signals.onObjDetCoords.emit(badmessage.objCoords)

                    elif badmessage.msgType == consts_pb2.MessageType.TELE_DRIVELINE_STATUS:
                        self.signals.onDrivelineStatus.emit(badmessage.drivelineStatus)
                        #pass

                    else:
                        #todo log we got something we do not understand
                        pass
                
                except Exception as ex:
                    print(ex)
            
            self.txMessage(self.bm_cmd_telemetry(False))

            print("Shutting down")

        except:
            print("GRPC Error")
            self.signals.onError.emit("exception")
        