from PySide2 import QtWidgets, QtCore, QtGui
import vlc

class VideoPlayer(QtWidgets.QWidget):

    def setPosition(self, position):
        self.player.set_position(position / 1000.0)

    def updateUI(self):
        self.positionSlider.setRange(0, 1000)
        if self.player.get_length() > 0:
            self.positionSlider.setValue(self.player.get_position() * 1000)
            self.positionSlider.setEnabled(True)
        else:
            self.positionSlider.setEnabled(False)

    def __init__(self, path, parent = None):
        super().__init__(parent)
        self.layout = QtWidgets.QVBoxLayout()
        self.secondLayout = QtWidgets.QHBoxLayout()
        self.widget = QtWidgets.QWidget()
        self.setLayout(self.layout)
        btnSize = QtCore.QSize(16, 16)

        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.media = self.instance.media_new(path)
        self.player.set_media(self.media)

        self.video = QtWidgets.QFrame()
        self.layout.addWidget(self.video)
        self.player.set_hwnd(self.video.winId())

        self.play_button = QtWidgets.QPushButton()
        self.play_button.setFixedSize(20, 20)
        self.play_button.setIconSize(btnSize)
        self.play_button.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaPlay))
        self.secondLayout.addWidget(self.play_button)
        self.play_button.clicked.connect(self.play_pause)

        self.stop_button = QtWidgets.QPushButton()
        self.stop_button.setFixedSize(20,20)
        self.stop_button.setIconSize(btnSize)
        self.stop_button.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaPlay))        
        self.secondLayout.addWidget(self.stop_button)

        self.stop_button.clicked.connect(self.stop)

        self.positionSlider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)
        self.secondLayout.addWidget(self.positionSlider)
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(200)
        self.timer.timeout.connect(self.updateSize)
        self.timer.timeout.connect(self.updateUI)
        self.layout.addLayout(self.secondLayout)
        self.timer.start()

    def play_pause(self):
        if self.player.get_state() == vlc.State.Playing:
            self.player.pause()
        else:
            self.player.play()

    def stop(self):
        self.player.stop()


    def updateSize(self):
        video_width = self.player.video_get_width()
        video_height = self.player.video_get_height()
        self.video.setGeometry(0, 0, video_width, video_height)


