from PySide2.QtCore import QObject, Signal, Slot
from PySide2.QtGui import QPixmap

class GraphicsSignals(QObject):
    onError = Signal(str)
    onLidarImageReady = Signal(QPixmap)
    onDrivelineImageReady = Signal(QPixmap)