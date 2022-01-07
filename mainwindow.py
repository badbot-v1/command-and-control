# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1146, 758)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.wd_horizon_attitude = QWidget(self.widget)
        self.wd_horizon_attitude.setObjectName(u"wd_horizon_attitude")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wd_horizon_attitude.sizePolicy().hasHeightForWidth())
        self.wd_horizon_attitude.setSizePolicy(sizePolicy)
        self.wd_horizon_attitude.setMaximumSize(QSize(380, 200))
        self.wd_horizon_attitude.setBaseSize(QSize(380, 0))

        self.gridLayout.addWidget(self.wd_horizon_attitude, 2, 3, 1, 1)

        self.wd_controls = QWidget(self.widget)
        self.wd_controls.setObjectName(u"wd_controls")
        self.wd_controls.setMaximumSize(QSize(450, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.wd_controls)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_2 = QGroupBox(self.wd_controls)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMaximumSize(QSize(350, 16777215))
        self.groupBox_2.setBaseSize(QSize(350, 0))
        self.formLayout_2 = QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_status_operational_mode = QLabel(self.groupBox_2)
        self.lbl_status_operational_mode.setObjectName(u"lbl_status_operational_mode")

        self.horizontalLayout_2.addWidget(self.lbl_status_operational_mode)

        self.dd_operational_mode = QComboBox(self.groupBox_2)
        self.dd_operational_mode.setObjectName(u"dd_operational_mode")

        self.horizontalLayout_2.addWidget(self.dd_operational_mode)


        self.formLayout_2.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_status_lidar_recording = QLabel(self.groupBox_2)
        self.lbl_status_lidar_recording.setObjectName(u"lbl_status_lidar_recording")

        self.horizontalLayout.addWidget(self.lbl_status_lidar_recording)

        self.btn_enable_lidar_recording = QPushButton(self.groupBox_2)
        self.btn_enable_lidar_recording.setObjectName(u"btn_enable_lidar_recording")

        self.horizontalLayout.addWidget(self.btn_enable_lidar_recording)

        self.btn_disable_lidar_recording = QPushButton(self.groupBox_2)
        self.btn_disable_lidar_recording.setObjectName(u"btn_disable_lidar_recording")

        self.horizontalLayout.addWidget(self.btn_disable_lidar_recording)


        self.formLayout_2.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_8)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btn_enable_app_video = QPushButton(self.groupBox_2)
        self.btn_enable_app_video.setObjectName(u"btn_enable_app_video")

        self.horizontalLayout_6.addWidget(self.btn_enable_app_video)

        self.btn_disable_app_video = QPushButton(self.groupBox_2)
        self.btn_disable_app_video.setObjectName(u"btn_disable_app_video")

        self.horizontalLayout_6.addWidget(self.btn_disable_app_video)


        self.formLayout_2.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_6)


        self.verticalLayout_3.addWidget(self.groupBox_2)


        self.gridLayout.addWidget(self.wd_controls, 2, 4, 1, 1)

        self.wd_status = QWidget(self.widget)
        self.wd_status.setObjectName(u"wd_status")
        self.wd_status.setMaximumSize(QSize(450, 250))
        self.wd_status.setBaseSize(QSize(0, 250))
        self.horizontalLayout_10 = QHBoxLayout(self.wd_status)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.tabWidget = QTabWidget(self.wd_status)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.South)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabSystemStatus = QWidget()
        self.tabSystemStatus.setObjectName(u"tabSystemStatus")
        self.verticalLayout_9 = QVBoxLayout(self.tabSystemStatus)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.widget_4 = QWidget(self.tabSystemStatus)
        self.widget_4.setObjectName(u"widget_4")
        self.formLayout_3 = QFormLayout(self.widget_4)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_6 = QLabel(self.widget_4)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.lbl_status_last_updated = QLabel(self.widget_4)
        self.lbl_status_last_updated.setObjectName(u"lbl_status_last_updated")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.lbl_status_last_updated)

        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.lbl_status_cpu_load = QLabel(self.widget_4)
        self.lbl_status_cpu_load.setObjectName(u"lbl_status_cpu_load")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.lbl_status_cpu_load)

        self.label_5 = QLabel(self.widget_4)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_3.setWidget(6, QFormLayout.LabelRole, self.label_5)

        self.lbl_status_memory = QLabel(self.widget_4)
        self.lbl_status_memory.setObjectName(u"lbl_status_memory")

        self.formLayout_3.setWidget(6, QFormLayout.FieldRole, self.lbl_status_memory)


        self.verticalLayout_9.addWidget(self.widget_4)

        self.tabWidget.addTab(self.tabSystemStatus, "")
        self.tabGpsDetails = QWidget()
        self.tabGpsDetails.setObjectName(u"tabGpsDetails")
        self.verticalLayout_10 = QVBoxLayout(self.tabGpsDetails)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_5 = QWidget(self.tabGpsDetails)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.widget_2 = QWidget(self.widget_5)
        self.widget_2.setObjectName(u"widget_2")
        self.formLayout = QFormLayout(self.widget_2)
        self.formLayout.setObjectName(u"formLayout")
        self.label_11 = QLabel(self.widget_2)
        self.label_11.setObjectName(u"label_11")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_11)

        self.lbl_status_lat = QLabel(self.widget_2)
        self.lbl_status_lat.setObjectName(u"lbl_status_lat")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lbl_status_lat)

        self.label_15 = QLabel(self.widget_2)
        self.label_15.setObjectName(u"label_15")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_15)

        self.lbl_status_lon = QLabel(self.widget_2)
        self.lbl_status_lon.setObjectName(u"lbl_status_lon")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lbl_status_lon)

        self.label_17 = QLabel(self.widget_2)
        self.label_17.setObjectName(u"label_17")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_17)

        self.lbl_status_hdop = QLabel(self.widget_2)
        self.lbl_status_hdop.setObjectName(u"lbl_status_hdop")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lbl_status_hdop)

        self.label_19 = QLabel(self.widget_2)
        self.label_19.setObjectName(u"label_19")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_19)

        self.lbl_status_vdop = QLabel(self.widget_2)
        self.lbl_status_vdop.setObjectName(u"lbl_status_vdop")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lbl_status_vdop)

        self.label_21 = QLabel(self.widget_2)
        self.label_21.setObjectName(u"label_21")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_21)

        self.lbl_status_pdop = QLabel(self.widget_2)
        self.lbl_status_pdop.setObjectName(u"lbl_status_pdop")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lbl_status_pdop)


        self.horizontalLayout_9.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.widget_5)
        self.widget_3.setObjectName(u"widget_3")
        self.formLayout_4 = QFormLayout(self.widget_3)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_12 = QLabel(self.widget_3)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_12)

        self.lbl_status_sat_visible = QLabel(self.widget_3)
        self.lbl_status_sat_visible.setObjectName(u"lbl_status_sat_visible")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.lbl_status_sat_visible)

        self.label_23 = QLabel(self.widget_3)
        self.label_23.setObjectName(u"label_23")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_23)

        self.lbl_status_sat_used = QLabel(self.widget_3)
        self.lbl_status_sat_used.setObjectName(u"lbl_status_sat_used")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.lbl_status_sat_used)

        self.label_25 = QLabel(self.widget_3)
        self.label_25.setObjectName(u"label_25")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_25)

        self.lbl_status_pressure = QLabel(self.widget_3)
        self.lbl_status_pressure.setObjectName(u"lbl_status_pressure")

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.lbl_status_pressure)

        self.label_27 = QLabel(self.widget_3)
        self.label_27.setObjectName(u"label_27")

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.label_27)

        self.lbl_status_altitude = QLabel(self.widget_3)
        self.lbl_status_altitude.setObjectName(u"lbl_status_altitude")

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.lbl_status_altitude)

        self.label_29 = QLabel(self.widget_3)
        self.label_29.setObjectName(u"label_29")

        self.formLayout_4.setWidget(4, QFormLayout.LabelRole, self.label_29)

        self.lbl_status_temperature = QLabel(self.widget_3)
        self.lbl_status_temperature.setObjectName(u"lbl_status_temperature")

        self.formLayout_4.setWidget(4, QFormLayout.FieldRole, self.lbl_status_temperature)


        self.horizontalLayout_9.addWidget(self.widget_3)


        self.verticalLayout_10.addWidget(self.widget_5)

        self.tabWidget.addTab(self.tabGpsDetails, "")

        self.horizontalLayout_10.addWidget(self.tabWidget)


        self.gridLayout.addWidget(self.wd_status, 2, 2, 1, 1)

        self.wd_lidar = QWidget(self.widget)
        self.wd_lidar.setObjectName(u"wd_lidar")
        sizePolicy.setHeightForWidth(self.wd_lidar.sizePolicy().hasHeightForWidth())
        self.wd_lidar.setSizePolicy(sizePolicy)
        self.wd_lidar.setMaximumSize(QSize(600, 600))
        self.wd_lidar.setBaseSize(QSize(600, 600))
        self.verticalLayout_2 = QVBoxLayout(self.wd_lidar)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_lidar_map = QLabel(self.wd_lidar)
        self.lbl_lidar_map.setObjectName(u"lbl_lidar_map")

        self.verticalLayout_2.addWidget(self.lbl_lidar_map)


        self.gridLayout.addWidget(self.wd_lidar, 1, 0, 2, 1)

        self.wd_planner = QWidget(self.widget)
        self.wd_planner.setObjectName(u"wd_planner")
        self.verticalLayout_8 = QVBoxLayout(self.wd_planner)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")

        self.gridLayout.addWidget(self.wd_planner, 0, 0, 1, 1)

        self.wd_video = QWidget(self.widget)
        self.wd_video.setObjectName(u"wd_video")
        self.wd_video.setEnabled(True)
        self.verticalLayout_4 = QVBoxLayout(self.wd_video)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.dd_stream = QComboBox(self.wd_video)
        self.dd_stream.setObjectName(u"dd_stream")

        self.horizontalLayout_3.addWidget(self.dd_stream)

        self.btn_play = QToolButton(self.wd_video)
        self.btn_play.setObjectName(u"btn_play")

        self.horizontalLayout_3.addWidget(self.btn_play)

        self.btn_stop = QToolButton(self.wd_video)
        self.btn_stop.setObjectName(u"btn_stop")

        self.horizontalLayout_3.addWidget(self.btn_stop)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.gridLayout.addWidget(self.wd_video, 0, 2, 2, 3)


        self.verticalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1146, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Command Console", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Operational Mode", None))
        self.lbl_status_operational_mode.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Lidar Recording", None))
        self.lbl_status_lidar_recording.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.btn_enable_lidar_recording.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.btn_disable_lidar_recording.setText(QCoreApplication.translate("MainWindow", u"Disable", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"App Video", None))
        self.btn_enable_app_video.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.btn_disable_app_video.setText(QCoreApplication.translate("MainWindow", u"Disable", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Last updated", None))
        self.lbl_status_last_updated.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"CPU Load", None))
        self.lbl_status_cpu_load.setText(QCoreApplication.translate("MainWindow", u"0.0 0.0 0.0", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"RAM / Swap", None))
        self.lbl_status_memory.setText(QCoreApplication.translate("MainWindow", u"348M / 4192M", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSystemStatus), QCoreApplication.translate("MainWindow", u"System Status", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Lat", None))
        self.lbl_status_lat.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Lon", None))
        self.lbl_status_lon.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"HDOP", None))
        self.lbl_status_hdop.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"VDOP", None))
        self.lbl_status_vdop.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"PDOP", None))
        self.lbl_status_pdop.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"#SAT Visible", None))
        self.lbl_status_sat_visible.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"#SAT used", None))
        self.lbl_status_sat_used.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Pressure", None))
        self.lbl_status_pressure.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Altitude", None))
        self.lbl_status_altitude.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.lbl_status_temperature.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGpsDetails), QCoreApplication.translate("MainWindow", u"GPS Details", None))
        self.lbl_lidar_map.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btn_play.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.btn_stop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
    # retranslateUi

