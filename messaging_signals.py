from PySide2.QtCore import QObject, Signal, Slot

from badbot_protos_pysrc import (
    botstatus_pb2,
    imudata_pb2,
    gpsdata_pb2,
    lidarscan_pb2,
    obj_det_coords_pb2,
    telemetry_pb2
)

class MessagingSignals(QObject):

    onError = Signal(str)
    onBotStatus = Signal(botstatus_pb2.BotStatus)
    onIMUData = Signal(imudata_pb2.ImuData)
    onGPSData = Signal(gpsdata_pb2.GpsData)
    onLidarScan = Signal(lidarscan_pb2.LidarScan, bool)
    onObjDetCoords = Signal(obj_det_coords_pb2.ObjectDetectionCoords)
    onDrivelineStatus = Signal(telemetry_pb2.DrivelineStatus)
    
