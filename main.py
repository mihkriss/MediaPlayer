from PyQt5.QtWidgets import *
import sys
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


# import shutil
# import startup.py


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Media Player")
        self.setGeometry(350, 100, 700, 500)
        self.setWindowIcon(QIcon('png-clipart-computer-icons-video-the-noun-project-angle-white.png'))

        self.setStyleSheet("background-color: white;")

        self.init_ui()

        self.show()

    def init_ui(self):
        self.filenameOpened = ''
        self.filenameFolder = ''
        self.filenameMask = ''
        self.filenameSaved = ''

        # create media player object
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        # create videowidget object

        videowidget = QVideoWidget()

        # create button for playing

        self.playBtn = QToolButton()
        self.playBtn.setEnabled(False)
        self.playBtn.setMinimumSize(60, 60)
        self.playBtn.setStyleSheet(
            "QToolButton {background-color: white; color: black; border-radius: 30px;  border: 2px groove gray;font: 9pt 'AcadEref';border-style: circle;}" "QToolButton:pressed {background-color:rgb(119, 136, 153) ; }")
        self.playBtn.setIconSize(self.playBtn.minimumSize())
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playBtn.clicked.connect(self.play_video)

        # create slider
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setStyleSheet("""
            QSlider{
                background: white;
            }
            QSlider::groove:horizontal {  
                height: 10px;
                margin: 0px;
                border-radius: 5px;
                background: #D3D3D3;
            }
            QSlider::handle:horizontal {
                background: #81848A;
                border: 1px solid #6D6F73;
                width: 17px;
                margin: -5px 0; 
                border-radius: 8px;
            }
            QSlider::sub-page:qlineargradient {
                background: rgb(119, 136, 153);
                border-radius: 5px;
            }
        """)
        self.slider.setRange(0, 0)
        self.slider.sliderMoved.connect(self.set_position)

        # create label
        self.label = QLabel()
        self.label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)

        # create hbox layout
        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setContentsMargins(0, 0, 0, 0)

        # set widgets to the hbox layout
        self.hboxLayout.addWidget(self.playBtn)
        self.hboxLayout.addWidget(self.slider)

        # create vbox layout
        self.vboxLayout = QVBoxLayout()
        self.vboxLayout.addWidget(videowidget)
        self.vboxLayout.addLayout(self.hboxLayout)
        self.vboxLayout.addWidget(self.label)

        self.BtnsLayout = QVBoxLayout()

        # OpenBtn
        self.openBtn = QPushButton('Open Video')
        self.openBtn.setFixedSize(160, 60)
        self.openBtn.setMinimumSize(70, 40)
        self.openBtn.setStyleSheet("QPushButton {background-color: #D3D3D3; color: black; border-radius: 20px;  border: 2px groove gray;font: 10pt 'Source Sans Pro';border-style: circle;}" "QPushButton:pressed {background-color:rgb(119, 136, 153);}")
        self.playBtn.setIconSize(self.playBtn.minimumSize())
        self.openBtn.clicked.connect(self.open_file)

        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setContentsMargins(0, 0, 0, 0)

        self.BtnsLayout.addWidget(self.openBtn)

        self.openlabel = QLabel()

        self.openlabel.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        self.BtnsLayout.addWidget(self.openlabel)
        self.openlabel.setText('')

        self.openlabel.setStyleSheet('''
            color: black; 
            padding-left: 200px;
        ''')

        # selectFolder
        self.selectFolder = QPushButton('Select folder')
        self.selectFolder.setFixedSize(160, 60)
        self.selectFolder.setMinimumSize(70, 40)
        self.selectFolder.setStyleSheet(
            "QPushButton {background-color: #D3D3D3; color: black; border-radius: 20px;  border: 2px groove gray;font: 10pt 'Source Sans Pro';border-style: circle;}" "QPushButton:pressed {background-color:rgb(119, 136, 153);}")
        self.playBtn.setIconSize(self.playBtn.minimumSize())

        self.selectFolder.clicked.connect(self.select_folder)

        self.BtnsLayout.addWidget(self.selectFolder)

        self.folderlabel = QLabel()
        self.folderlabel.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        self.BtnsLayout.addWidget(self.folderlabel)
        self.folderlabel.setText('')
        self.folderlabel.setStyleSheet('''
                    color: black; 
                    padding-left: 200px;
                ''')

        # selectMask
        self.selectMask = QPushButton('Select mask folder')
        self.selectMask.setFixedSize(160, 60)
        self.selectMask.setMinimumSize(70, 40)
        self.selectMask.setStyleSheet(
            "QPushButton {background-color: #D3D3D3; color: black; border-radius: 20px;  border: 2px groove gray;font: 9pt 'Source Sans Pro';border-style: circle;}" "QPushButton:pressed {background-color:rgb(119, 136, 153);}")
        self.playBtn.setIconSize(self.playBtn.minimumSize())
        self.selectMask.clicked.connect(self.select_mask)
        self.BtnsLayout.addWidget(self.selectMask)

        self.masklabel = QLabel()
        self.masklabel.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        self.BtnsLayout.addWidget(self.masklabel)
        self.masklabel.setText('')
        self.masklabel.setStyleSheet('''
                    color: black;
                    padding-left: 200px;
                ''')

        # create save button
        self.saveBtn = QPushButton('Save Video as')
        self.saveBtn.setFixedSize(160, 60)
        self.saveBtn.setMinimumSize(70, 40)
        self.saveBtn.setStyleSheet(
            "QPushButton {background-color: #D3D3D3; color: black; border-radius: 20px;  border: 2px groove gray;font: 10pt 'Source Sans Pro';border-style: circle;}" "QPushButton:pressed {background-color:rgb(119, 136, 153);}" "QLabel { font: bold italic }")
        self.playBtn.setIconSize(self.playBtn.minimumSize())
        self.hbox1 = QHBoxLayout()
        self.hbox1.addStretch(1)
        self.hbox1.addWidget(self.saveBtn)
        self.hbox1.addWidget(self.saveBtn)
        self.saveBtn.clicked.connect(self.save_file)
        self.BtnsLayout.addWidget(self.saveBtn)

        self.vboxLayout.addLayout(self.BtnsLayout)
        self.setLayout(self.vboxLayout)

        self.mediaPlayer.setVideoOutput(videowidget)


        # media player signals

        self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)

    def open_file(self):
        self.filenameOpened, _ = QFileDialog.getOpenFileName(self, "Open Video")
        if self.filenameOpened != '':
            self.openlabel.setText(self.filenameOpened)
            self.folderlabel.setText('')
            self.filenameFolder = ''
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(self.filenameOpened)))
            self.playBtn.setEnabled(True)

    def save_file(self):
        self.filenameSaved, _ = QFileDialog.getSaveFileName(self, "Save Video")

        if self.filenameOpened != '' and self.filenameSaved != '' and self.filenameMask != '':
            # shutil.copy2(self.filenameOpened, self.filenameSaved)
            # new:
            ## process_video('/'.join(self.filenameOpened.split('/')[:-1]), self.filenameMask, self.filenameSaved, self.filenameOpened.split('/')[-1])
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(self.filenameSaved)))
            self.filenameOpened = ''
            self.filenameFolder = ''
            self.filenameMask = ''
            self.filenameSaved = ''

            self.masklabel.setText('')
            self.openlabel.setText('')

            self.playBtn.setEnabled(True)
        elif self.filenameFolder != '' and self.filenameSaved != '' and self.filenameMask != '':
            # shutil.copy2(self.filenameOpened, self.filenameSaved)
            # new:
            ## process_video(self.filenameFolder, self.filenameMask, self.filenameSaved)
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(self.filenameSaved)))
            self.filenameOpened = ''
            self.filenameFolder = ''
            self.filenameMask = ''
            self.filenameSaved = ''

            self.masklabel.setText('')
            self.folderlabel.setText('')

            self.playBtn.setEnabled(True)

    def play_video(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()

        else:
            self.mediaPlayer.play()

    def mediastate_changed(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playBtn.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPause)

            )

        else:
            self.playBtn.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPlay)

            )

    def position_changed(self, position):
        self.slider.setValue(position)

    def duration_changed(self, duration):
        self.slider.setRange(0, duration)

    def set_position(self, position):
        self.mediaPlayer.setPosition(position)

    def handle_errors(self):
        self.playBtn.setEnabled(False)
        self.label.setText("Error: " + self.mediaPlayer.errorString())

    def select_folder(self):
        self.filenameFolder = QFileDialog.getExistingDirectory(self, "Select folder")
        if self.filenameFolder != '':
            self.filenameOpened = ''
            self.openlabel.setText('')
            self.folderlabel.setText(self.filenameFolder)
        self.filenameOpened = ''

    def select_mask(self):
        self.filenameMask = QFileDialog.getExistingDirectory(self, "Select mask")
        if self.filenameMask != '':
            self.masklabel.setText(self.filenameMask)


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
