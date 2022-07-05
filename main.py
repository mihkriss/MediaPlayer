from PyQt5.QtWidgets import *
import sys
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Media Player")
        self.setGeometry(350, 100, 700, 500)
        self.setWindowIcon(QIcon('png-clipart-computer-icons-video-the-noun-project-angle-white.png'))
        p =self.palette()
        p.setColor(QPalette.Window, Qt.white)
        self.setPalette(p)

        self.init_ui()


        self.show()


    def init_ui(self):

        #create media player object
        self.mediaPlayer1 = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaPlayer2 = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        #create videowidget object

        videowidget1 = QVideoWidget()
        videowidget2 = QVideoWidget()

        #create open button
        zn = QIcon()
        zn.addPixmap(QPixmap("png-clipart-computer-icons-video-angle-rectangle.png"))
        self.openBtn1 = QToolButton()
        self.openBtn1.setIcon(zn)
        self.openBtn1.clicked.connect(lambda: self.open_file(self.mediaPlayer1, self.playBtn1))
        #openBtn2 = QPushButton('Open Video')
        #openBtn2.clicked.connect(lambda: self.open_file(self.mediaPlayer2, self.playBtn2))


        #create button for playing

        icon = QIcon()
        icon.addPixmap(QPixmap("img_68465.png"))

        self.playBtn1 = QToolButton()
        self.playBtn1.setIcon(icon)
        self.playBtn1.setEnabled(False)

        self.playBtn1.clicked.connect(lambda: self.play_video(self.mediaPlayer1))
        self.playBtn2 = QToolButton()
        self.playBtn2.setEnabled(False)
        self.playBtn2.setIcon(icon)
        self.playBtn2.clicked.connect(lambda: self.play_video(self.mediaPlayer2))



        #create slider
        self.slider1 = QSlider(Qt.Horizontal)
        self.slider1.setRange(0, 0)
        self.slider1.sliderMoved.connect(self.set_position1)
        self.slider2 = QSlider(Qt.Horizontal)
        self.slider2.setRange(0, 0)
        self.slider2.sliderMoved.connect(self.set_position2)



        #create label
        self.label1 = QLabel()
        self.label1.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        self.label2 = QLabel()
        self.label2.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        self.filename = ''

        #create hbox layout
        hboxLayout1 = QHBoxLayout()
        hboxLayout1.setContentsMargins(0, 0, 0, 0)
        hboxLayout2 = QHBoxLayout()
        hboxLayout2.setContentsMargins(0, 0, 0, 0)

        #set widgets to the hbox layout
        hboxLayout1.addWidget(self.openBtn1)
        hboxLayout1.addWidget(self.playBtn1)
        hboxLayout1.addWidget(self.slider1)
        #hboxLayout2.addWidget(openBtn2)
        hboxLayout2.addWidget(self.playBtn2)
        hboxLayout2.addWidget(self.slider2)



        #create vbox layout
        vboxLayout1 = QVBoxLayout()
        vboxLayout1.addWidget(videowidget1)
        vboxLayout1.addLayout(hboxLayout1)
        vboxLayout1.addWidget(self.label1)
        vboxLayout2 = QVBoxLayout()
        vboxLayout2.addWidget(videowidget2)
        vboxLayout2.addLayout(hboxLayout2)
        vboxLayout2.addWidget(self.label2)

        newLayout = QVBoxLayout()
        newLayout.addLayout(vboxLayout1)

        icon1 = QIcon()
        icon1.addPixmap(QPixmap("Down-Arrow-Transparent-Image.png"))

        self.bigBtn = QToolButton()
        self.bigBtn.setIcon(icon1)
        self.bigBtn.setGeometry(QRect(220, 120, 41, 41))
        self.bigBtn.setEnabled(False)
        self.bigBtn.clicked.connect(self.do_smthing_with_videofile)

        newLayout.addWidget(self.bigBtn)

        newLayout.addLayout(vboxLayout2)

        self.setLayout(newLayout)

        self.mediaPlayer1.setVideoOutput(videowidget1)
        self.mediaPlayer2.setVideoOutput(videowidget2)


        #sound
        hbox = QHBoxLayout()
        self.slider = QSlider()
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(1)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.valueChanged.connect(self.changedValue)
        self.label = QLabel("0")
        self.label.setFont(QFont("Sanserif", 15))
        hbox.addWidget(self.slider)
        hbox.addWidget(self.label)
        self.setLayout(hbox)
        self.slider.show()


        self.mediaPlayer1.stateChanged.connect(lambda: self.mediastate_changed(self.mediaPlayer1, self.playBtn1))
        self.mediaPlayer1.positionChanged.connect(self.position_changed1)
        self.mediaPlayer1.durationChanged.connect(self.duration_changed1)
        self.mediaPlayer2.stateChanged.connect(lambda: self.mediastate_changed(self.mediaPlayer2, self.playBtn2))
        self.mediaPlayer2.positionChanged.connect(self.position_changed2)
        self.mediaPlayer2.durationChanged.connect(self.duration_changed2)

    def open_file(self, player, btn):
        self.filename, _ = QFileDialog.getOpenFileName(self, "Open Video")

        if self.filename != '':
            player.setMedia(QMediaContent(QUrl.fromLocalFile(self.filename)))
            btn.setEnabled(True)
            self.bigBtn.setEnabled(True)
    def play_video(self, player):
        if player.state() == QMediaPlayer.PlayingState:
            player.pause()

        else:
            player.play()

    def mediastate_changed(self, player, btn):
        if player.state() == QMediaPlayer.PlayingState:
            btn.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPause)

            )
        else:
            btn.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPlay)

            )

    def changedValue(self):
        size = self.slider.value()
        self.label.setText(str(size))

    def position_changed1(self, position):
        self.slider1.setValue(position)
    def position_changed2(self, position):
        self.slider2.setValue(position)


    def duration_changed1(self, duration):
        self.slider1.setRange(0, duration)
    def duration_changed2(self, duration):
        self.slider2.setRange(0, duration)

    def set_position1(self, position):
        self.mediaPlayer1.setPosition(position)
    def set_position2(self, position):
        self.mediaPlayer2.setPosition(position)


    def handle_errors1(self):
        self.playBtn1.setEnabled(False)
        self.label1.setText("Error: " + self.mediaPlayer1.errorString())
    def handle_errors2(self):
        self.playBtn2.setEnabled(False)
        self.label2.setText("Error: " + self.mediaPlayer2.errorString())

    def do_smthing_with_videofile(self):
        self.mediaPlayer2.setMedia(QMediaContent(QUrl.fromLocalFile(self.filename)))
        self.playBtn2.setEnabled(True)


        volumeDescBtn = QPushButton('V (-)')  # Decrease Volume
        volumeIncBtn = QPushButton('V (+)')  # Increase Volume
        volumeDescBtn.clicked.connect(self.decreaseVolume)
        volumeIncBtn.clicked.connect(self.increaseVolume)

        self.player = QMediaPlayer()
        self.player.volumeChanged.connect(self.qmp_volumeChanged)
        self.player.setVolume(60)
    def increaseVolume(self):
        vol = self.player.volume()
        vol = min(vol + 5, 100)
        self.player.setVolume(vol)


    def decreaseVolume(self):
        vol = self.player.volume()
        vol = max(vol - 5, 0)
        self.player.setVolume(vol)

    def qmp_volumeChanged(self):
        msg = self.statusBar().currentMessage()
        msg = msg[:-2] + str(self.player.volume())
        self.statusBar().showMessage(msg)


# media player signals


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())