from PySide2.QtCore import QObject, Signal, Slot
from PySide2.QtGui import QPixmap

class GamepadSignals(QObject):
    onY = Signal(int)
    onX = Signal(int)

class GamepadStreamSignals(QObject):
    onStream = Signal(int,int)
