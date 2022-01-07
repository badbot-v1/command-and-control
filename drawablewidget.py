from PySide2.QtWidgets import QWidget, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem, QVBoxLayout, QGraphicsRectItem, QGraphicsPixmapItem
from PySide2.QtMultimedia import QMediaPlayer
from PySide2.QtMultimediaWidgets import QVideoWidget, QGraphicsVideoItem
from PySide2.QtGui import QPainter, QColor, QFont, QBrush, QPen
from PySide2.QtCore import QSize, Qt, QRectF, QUrl, Slot

class DrawableWidget(QWidget):
    def __init__(self, parent=None):
        super(DrawableWidget, self).__init__(parent)

        self._scene = QGraphicsScene(self)
        self._gv = QGraphicsView(self._scene)
        self._gv.setBackgroundBrush(QBrush(Qt.black))

        self._videoitem = QGraphicsVideoItem()
        self._scene.addItem(self._videoitem)
        self._videoitem.setSize(QSize(640,480))
        self._roi_item = QGraphicsRectItem(QRectF(50, 50, 40, 40), self._videoitem)
        self._roi_item.setBrush(QBrush(QColor(0,0,255,100)))
        self._roi_item.setPen(QPen(Qt.red))

        self._roi_kf_reported = QGraphicsRectItem(QRectF(10, 10, 20, 20), self._videoitem)
        self._roi_kf_reported.setBrush(QBrush(QColor(0,0,255,100)))
        self._roi_kf_reported.setPen(QPen(Qt.yellow))

        self._drivelineHistory = QGraphicsPixmapItem(self._videoitem)
        self._drivelineHistory.setOffset(0,0)
        
        self._player = QMediaPlayer(self, QMediaPlayer.VideoSurface)
        self._player.setVideoOutput(self._videoitem)
        self._player.stateChanged.connect(self.on_stateChanged)

        # file = os.path.join(os.path.dirname(__file__), "small.mp4")
        # self._player.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(file)))
        # button = QtWidgets.QPushButton("Play")
        # button.clicked.connect(self._player.play)

        self.resize(640, 480)
        lay = QVBoxLayout(self)
        lay.addWidget(self._gv)
        # lay.addWidget(button)
    
    @Slot(QMediaPlayer.State)
    def on_stateChanged(self, state):
        pass
        # if state == QMediaPlayer.PlayingState:
        #     self._gv.fitInView(self._videoitem, Qt.KeepAspectRatio)
            
    def playVideo(self, url):

        self._video_url = url

        self._player.stop()
        self._player.setMedia(QUrl(url))
        self._player.play()

    def startVideo(self):
        if self._video_url is not None:
            self.playVideo(self._video_url)
    
    def stopVideo(self):
        self._player.stop()

    def updateRect(self, y, x, h, w):
        self._roi_item.setRect(x,y,w,h)

    def updateDriveline(self, pixmap):
        self._drivelineHistory.setPixmap(pixmap)

    def updateRoiKfEstimate(self, mid):
        self._roi_kf_reported.setRect(mid, 100, 20, 20)
    
        
