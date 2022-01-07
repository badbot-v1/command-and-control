from pyPS4Controller.controller import Controller
from PySide2.QtCore import QRunnable, Signal, Slot, QFile

from gamepad_signals import GamepadSignals, GamepadStreamSignals
import time

class GamepadController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
        self.signals = GamepadSignals()
        self.threshold = 2000
        self.keep_running = True

    def getScaledValue(self, OldValue, OldMin=0, OldMax=32000, NewMin=0, NewMax=254):
        OldRange = (OldMax - OldMin)
        if OldRange == 0:
            NewValue = NewMin
        else:
            NewRange = (NewMax - NewMin)  
            NewValue = (((OldValue - OldMin) * NewRange) / OldRange) + NewMin
        
        if NewValue > NewMax:
            NewValue = NewMax
        elif NewValue < NewMin:
            NewValue = NewMin
        
        return NewValue
        

    #left joystick
    def on_L3_y_at_rest(self):
        self.signals.onY.emit(0)

    def on_L3_up(self,v):
        val = abs(v)
        if val > self.threshold:
            self.signals.onY.emit(int(self.getScaledValue(v*-1)))
        else:
            self.signals.onY.emit(0)

    def on_L3_down(self,v):
        val = abs(v)
        if val > self.threshold:
            self.signals.onY.emit(int(self.getScaledValue(v)*-1.0))
        else:
            self.signals.onY.emit(0)
    
    def on_L3_right(self,v):
        pass

    def on_L3_left(self,v):
        pass

    #right joystick
    def on_R3_x_at_rest(self):
        self.signals.onX.emit(0)

    def on_R3_right(self, v):
        val = abs(v)
        if val > self.threshold:
            self.signals.onX.emit(int(self.getScaledValue(v)))
        else:
            self.signals.onX.emit(0)

    def on_R3_left(self, v):
        val = abs(v)
        if val > self.threshold:
            self.signals.onX.emit(int(self.getScaledValue(v*-1)*-1))
        else:
            self.signals.onX.emit(0)

    def on_R3_up(self, v):
        pass

    def on_R3_down(self, v):
        pass

class GamepadListener(QRunnable):
    def __init__(self):
        super().__init__()
        self.controller = GamepadController(interface="/dev/input/js0", connecting_using_ds4drv=False)

    @Slot()
    def run(self):
        self.controller.listen()
        print("GamepadListener exited")


class GamepadStreamer(QRunnable):
    def __init__(self, threadpool):
        super().__init__()

        self.signals = GamepadStreamSignals()
        self.keep_running = True
        self.eventingInterval = 0.1
        self.lastValY = 0
        self.lastValX = 0
        self.thread_pool = threadpool

    def setup(self):
        self.gamepadlistener = GamepadListener()
        self.gamepadlistener.controller.signals.onY.connect(self.onGamepadY)
        self.gamepadlistener.controller.signals.onX.connect(self.onGamepadX)
        self.thread_pool.start(self.gamepadlistener)
        
    @Slot()
    def onGamepadY(self, val):
        self.lastValY = val
        
    
    @Slot()
    def onGamepadX(self, val):
        self.lastValX = val
        

    @Slot()
    def run(self):

        while self.keep_running:

            try:
                self.signals.onStream.emit(self.lastValY, self.lastValX)
            except Exception as ex:
                print(ex)
                break

            time.sleep(self.eventingInterval)
        
        self.gamepadlistener.stop = True

        print("GamepadStreamer exited")
