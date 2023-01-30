from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtMultimediaWidgets import QVideoWidget
# import vlc

class VideoPlayer(QtWidgets.QWidget):
    def __init__(self, path, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Video Player")
        self.setGeometry(200, 200, 600, 400)
        self.setMinimumSize(600, 400)
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        self.player = self.init_player(path)
        self.video = self.init_video()
        self.controls = self.init_controls()
        

        self.layout.addWidget(self.video, stretch=1)
        self.layout.addLayout(self.controls)

    def init_player(self, path):
        instance = vlc.Instance("--vout mmal_vout")
        player = instance.media_player_new()
        media = instance.media_new(path)
        player.set_media(media)
        return player

    def init_video(self):
        video = QtWidgets.QFrame()
        video.setFrameShape(QtWidgets.QFrame.Box)
        video.setLineWidth(1)
        video.setMidLineWidth(1)
        video.setAutoFillBackground(True)
        video.setPalette(QtGui.QPalette(QtGui.QColor(0, 0, 0)))
        video.setAttribute(QtCore.Qt.WA_NativeWindow, True)
        video.winId()
        self.player.set_hwnd(video.winId())
        return video

    def init_controls(self):
        controls = QtWidgets.QHBoxLayout()
        self.play_button = QtWidgets.QPushButton()
        self.play_button.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaPlay))
        self.play_button.clicked.connect(self.play_pause)
        controls.addWidget(self.play_button)
        
        self.stop_button = QtWidgets.QPushButton()
        self.stop_button.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaStop)) 
        self.stop_button.clicked.connect(self.stop)
        controls.addWidget(self.stop_button)

        self.positionSlider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.positionSlider.setRange(0, 1000)
        self.positionSlider.setEnabled(False)
        self.positionSlider.sliderMoved.connect(self.setPosition)
        controls.addWidget(self.positionSlider)
        self.volume = self.init_volume()
        self.mute_button = self.init_mute_button()
        controls.addLayout(self.volume)
        controls.addWidget(self.mute_button)


        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(200)
        self.timer.timeout.connect(self.updateUI)
        self.timer.start()


        
        return controls

    def play_pause(self):
        if self.player.get_state() == vlc.State.Playing:            
            self.play_button.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaPlay))
            self.player.pause()
        else:
            self.player.play()
            self.play_button.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaPause))

    def stop(self):
        self.player.stop()

    def setPosition(self, position):
        self.player.set_position(position / 1000.0)

    def updateUI(self):
        self.positionSlider.setRange(0, 1000)
        if self.player.get_length() > 0:
            self.positionSlider.setValue(self.player.get_position() * 1000)
            self.positionSlider.setEnabled(True)
        else:
            self.positionSlider.setEnabled(False)
        

    def init_volume(self):
        volume = QtWidgets.QHBoxLayout()
        self.volume_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(100)
        self.volume_slider.valueChanged.connect(self.set_volume)
        volume.addWidget(QtWidgets.QLabel("Volume:"))
        volume.addWidget(self.volume_slider)
        return volume

    def init_mute_button(self):
        self.mute_button = QtWidgets.QPushButton("Mute")
        self.mute_button.clicked.connect(self.toggle_mute)
        return self.mute_button

    def set_volume(self, volume):
        self.player.audio_set_volume(volume)

    def toggle_mute(self):
        if self.player.audio_get_mute() == 1:
            self.player.audio_set_mute(0)
            self.mute_button.setText("Mute")
        else:
            self.player.audio_set_mute(1)
            self.mute_button.setText("Unmute")


