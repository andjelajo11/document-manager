from PySide2 import QtWidgets, QtCore, QtMultimedia, QtGui
import os

class AudioPlayer(QtWidgets.QWidget):
    def __init__(self, path, parent = None):
        
        super().__init__(parent)
        label = QtWidgets.QLabel()
        label.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        label.setFont(font)
        file_name = os.path.basename(path).split(".")[0]

        label.setText(str(file_name))
        self.setWindowTitle("Video Player")
        self.setGeometry(200, 200, 600, 400)
        self.setMinimumSize(600, 400)
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        self.player = self.init_player(path)
        self.controls = self.init_controls()

        self.layout.addWidget(label)

        self.layout.addLayout(self.controls)

    def init_player(self, path):
        player = QtMultimedia.QMediaPlayer(self)
        player.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(path)))
        player.positionChanged.connect(self.updateUI)

        return player
    
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
        if self.player.state() == QtMultimedia.QMediaPlayer.PlayingState:
            self.play_button.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaPlay))
            self.player.pause()
        else:
            self.player.play()
            self.play_button.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaPause))

    def stop(self):
        self.player.stop()

    def setPosition(self, position):
        self.player.setPosition(position)


    def updateUI(self):
        self.positionSlider.setRange(0, self.player.duration())
        if self.player.duration() > 0:
            self.positionSlider.setValue(self.player.position())
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
        self.muted = 0
        self.mute_button.clicked.connect(self.toggle_mute)
        return self.mute_button

    def set_volume(self, volume):
        self.player.setVolume(volume)

    def toggle_mute(self):
        if self.muted == 0:
            self.player.setMuted(True)
            self.mute_button.setText("Unmute")
            self.muted = 1
        else:
            self.player.setMuted(False)
            self.mute_button.setText("Mute")
            self.muted = 0

