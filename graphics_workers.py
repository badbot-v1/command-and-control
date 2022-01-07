import time
import logging
import queue
import math
import copy

import graphics_signals
from PySide2.QtCore import QRunnable, Signal, Slot, QFile, QPoint
from PySide2.QtGui import QPixmap, QPainter, QColor, QPen, QFont

from badbot_protos_pysrc import (
    lidarscan_pb2
)

class GraphicsWorkers(QRunnable):
    def __init__(self):
        super().__init__()
        self.keep_running = True
        self.signals = graphics_signals.GraphicsSignals()
        self.lidarProcessQueue = queue.Queue(0)
        self.lidarPoiQueue = None
        self.drivelineStatusHistory = []

        #drawing assistance - should come from config
        self.x_pixels_per_ft = 10
        self.y_pixels_per_ft = 10

        self._person_at_angle = 0

        self.createDefaultMaps()

    def createDefaultMaps(self):

        pen_angles_color_1 = QPen(QColor(50,50,50),1)
        color_black = QColor(0,0,0)

        self.lidar_canvas = QPixmap(400,400)
        self.lidar_canvas.fill(color_black)
        painter = QPainter(self.lidar_canvas)

        painter.setPen(pen_angles_color_1)
        
        #draw angle lines
        for i in range(0, 360, 45):
            x2 = 200 + (math.cos(math.radians(i) ) * 150)
            y2 = 200 + (math.sin(math.radians(i) ) * 150)
            painter.drawLine(200, 200, x2, y2)
            painter.drawText(x2,y2,"{}".format(i))

        painter.end()
            
    
    def enqueueLidarScanForProcessing(self, data, ispoi):
        if ispoi is False:
            self.lidarProcessQueue.put_nowait(data)
        else:
            self.lidarPoiQueue = data
    
    def enqueueDrivelineStatusForProcessing(self, data):
        self.drivelineStatusHistory.append((data.vLeft, data.vRight))

        if len(self.drivelineStatusHistory) > 640:
            self.drivelineStatusHistory = self.drivelineStatusHistory[-640:]

        #print(self.drivelineStatusHistory)
    
    def autoDelete(self):
        return False

    @Slot()
    def run(self):

        print("Graphics worker started")
        pen_lidar = QPen(QColor(255,0,0),1)
        pen_lidar_poi = QPen(QColor(255,255,0),5)
        pen_lidar_scan_fov = QPen(QColor(0,255,0),1)
        color_bg_transparent = QColor(0,0,0,0)

        pens_red = {}
        pens_green= {}

        for i in range(0,256):
            color_value = 100+i if 100+i < 256 else 255
            pens_red[i]  = QPen(QColor(color_value,0,0), 6)
            pens_green[i] = QPen(QColor(0,color_value,0), 6)


        x1 = 200
        y1 = 200
        mount_diff_rads = -0.20943958
        img_rotation_rads = 0 #-1.74533
        self.total_rotation_rads = mount_diff_rads + img_rotation_rads


        # frame_counter=0
        while self.keep_running is True:


            #if we have regular lidar data, draw it on canvas                  
            if self.lidarProcessQueue.qsize() > 0:
            
                try:
                    #draw the canvas
                    canvas = self.lidar_canvas.copy()
                    painter = QPainter(canvas)

                    #draw the fov for lidar to find objects of interest
                    painter.setPen(pen_lidar_scan_fov)

                    

                    for i in [-10,10]:
                        person_at = math.radians(self._person_at_angle + i)
                        # x2 = 200 + (math.cos(self._person_at_angle + math.radians(i) + self.total_rotation_rads) * 100)
                        # y2 = 200 + (math.sin(self._person_at_angle + math.radians(i) + self.total_rotation_rads) * 100)
                        x2 = 200 + math.cos(person_at) * 100
                        y2 = 200 + math.sin(person_at) * 100

                        painter.drawLine(x1, y1, x2, y2)

                    currScan = self.lidarProcessQueue.get(False)
                    painter.setPen(pen_lidar)

                    self.plotLidarPoints(painter, currScan.scanpoints)

                    #if we have poi lidar data, draw it on canvas                  
                    if self.lidarPoiQueue is not None:
                    
                        try:
                            painter.setPen(pen_lidar_poi)
                            self.plotLidarPoints(painter, self.lidarPoiQueue.scanpoints)
                            
                        except:
                            if self.keep_running is not True:
                                break

                    painter.end()
                    self.signals.onLidarImageReady.emit(canvas)
                    
                except:
                    #todo log here
                    if self.keep_running is not True:
                        break

            drivelineScan = list.copy(self.drivelineStatusHistory)
            
            if len(drivelineScan) > 0:
            
                canvas = QPixmap(640,60)
                canvas.fill(color_bg_transparent)
                painter = QPainter(canvas)
                
                #draw the latest velocities
                vLeft, vRight = drivelineScan[len(drivelineScan)-1]
                painter.setPen(pens_red[255])
                painter.setFont(QFont('Decorative', 10))
                painter.drawText(QPoint(0,26), "L{}".format(vLeft))
                painter.setPen(pens_green[255])
                painter.drawText(QPoint(50,26), "R{}".format(vRight))

                for i in range(0, len(drivelineScan)):
                    vLeft, vRight = drivelineScan[i]
                    # vLeft = 100 if vLeft == 255 else vLeft
                    # vRight = 100 if vRight == 255 else vRight
                    
                    #vLeft is red
                    painter.setPen(pens_red[vLeft])
                    painter.drawPoint(i, 5)

                    #vRight is blue
                    painter.setPen(pens_green[vRight])
                    painter.drawPoint(i, 10)
                
                painter.end()

                self.signals.onDrivelineImageReady.emit(canvas)

            time.sleep(0.03)

        print("Graphics worker exited")

    def plotLidarPoints(self, painter, points):
        for point in points:
            #px = 200 + (math.cos(point.angle - 0.261799) * point.range) * self.x_pixels_per_ft
            #py = 200 + (math.sin(point.angle - 0.261799) * point.range) * self.y_pixels_per_ft
            px = 200 + (math.cos(point.angle + self.total_rotation_rads) * point.range) * self.x_pixels_per_ft
            py = 200 + (math.sin(point.angle + self.total_rotation_rads) * point.range) * self.y_pixels_per_ft

            painter.drawPoint(px, py)
