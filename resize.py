import sys
import cv2
import numpy as np
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QImage, QPixmap

class ZoomWindow(QtWidgets.QWidget):
    def __init__(self, image, scaleFactor):
        super().__init__()
        self.image = image
        self.scaleFactor = scaleFactor
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Zoomed Image')
        self.imageLabel = QtWidgets.QLabel(self)
        self.displayImage(self.scaleFactor)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.imageLabel)
        self.setLayout(layout)

    def displayImage(self, scaleFactor):
        height, width, channel = self.image.shape
        newWidth = int(width * scaleFactor)
        newHeight = int(height * scaleFactor)
        resizedImage = cv2.resize(self.image, (newWidth, newHeight), interpolation=cv2.INTER_AREA)
        qImg = QImage(resizedImage.data, newWidth, newHeight, newWidth * channel, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qImg)
        self.imageLabel.setPixmap(pixmap)
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1736, 848)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.imageLabel = QtWidgets.QLabel(self.centralwidget)
        self.imageLabel.setGeometry(QtCore.QRect(540, 20, 720, 480))
        self.imageLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.imageLabel.setText("")
        self.imageLabel.setObjectName("imageLabel")
        self.imageButton = QtWidgets.QPushButton(self.centralwidget)
        self.imageButton.setGeometry(QtCore.QRect(780, 530, 200, 75))
        self.imageButton.setObjectName("imageButton")
        self.button2x = QtWidgets.QPushButton(self.centralwidget)
        self.button2x.setGeometry(QtCore.QRect(570, 610, 200, 75))
        self.button2x.setObjectName("button2x")
        self.button3x = QtWidgets.QPushButton(self.centralwidget)
        self.button3x.setGeometry(QtCore.QRect(780, 610, 200, 75))
        self.button3x.setObjectName("button3x")
        self.button4x = QtWidgets.QPushButton(self.centralwidget)
        self.button4x.setGeometry(QtCore.QRect(1000, 610, 200, 75))
        self.button4x.setObjectName("button4x")
        self.button_2x = QtWidgets.QPushButton(self.centralwidget)
        self.button_2x.setGeometry(QtCore.QRect(570, 680, 200, 75))
        self.button_2x.setObjectName("button_2x")
        self.button_3x = QtWidgets.QPushButton(self.centralwidget)
        self.button_3x.setGeometry(QtCore.QRect(780, 680, 200, 75))
        self.button_3x.setObjectName("button_3x")
        self.button_4x = QtWidgets.QPushButton(self.centralwidget)
        self.button_4x.setGeometry(QtCore.QRect(1000, 680, 200, 75))
        self.button_4x.setObjectName("button_4x")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1736, 24))
        self.menubar.setObjectName("menubar")
        self.menuRotasi = QtWidgets.QMenu(self.menubar)
        self.menuRotasi.setObjectName("menuRotasi")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_45 = QtWidgets.QAction(MainWindow)
        self.action_45.setObjectName("action_45")
        self.action45 = QtWidgets.QAction(MainWindow)
        self.action45.setObjectName("action45")
        self.action_90 = QtWidgets.QAction(MainWindow)
        self.action_90.setObjectName("action_90")
        self.action90 = QtWidgets.QAction(MainWindow)
        self.action90.setObjectName("action90")
        self.action180 = QtWidgets.QAction(MainWindow)
        self.action180.setObjectName("action180")
        self.menuRotasi.addAction(self.action_45)
        self.menuRotasi.addAction(self.action45)
        self.menuRotasi.addAction(self.action_90)
        self.menuRotasi.addAction(self.action90)
        self.menuRotasi.addAction(self.action180)
        self.menubar.addAction(self.menuRotasi.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.imageButton.clicked.connect(self.loadImage)
        self.button2x.clicked.connect(lambda: self.openZoomWindow(2.0))
        self.button3x.clicked.connect(lambda: self.openZoomWindow(3.0))
        self.button4x.clicked.connect(lambda: self.openZoomWindow(4.0))
        self.button_2x.clicked.connect(lambda: self.openZoomWindow(0.5))
        self.button_3x.clicked.connect(lambda: self.openZoomWindow(1/3))
        self.button_4x.clicked.connect(lambda: self.openZoomWindow(0.25))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.imageButton.setText(_translate("MainWindow", "Load Image"))
        self.button2x.setText(_translate("MainWindow", "2x"))
        self.button3x.setText(_translate("MainWindow", "3x"))
        self.button4x.setText(_translate("MainWindow", "4x"))
        self.button_2x.setText(_translate("MainWindow", "1/2x"))
        self.button_3x.setText(_translate("MainWindow", "1/3x"))
        self.button_4x.setText(_translate("MainWindow", "1/4x"))

    def loadImage(self):
        self.image = cv2.imread('1311975.jpg')
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)  # Convert from BGR to RGB
        self.displayImage()

    def displayImage(self):
        height, width, channel = self.image.shape
        qImg = QImage(self.image.data, width, height, width * channel, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qImg).scaled(self.imageLabel.width(), self.imageLabel.height(), QtCore.Qt.KeepAspectRatio)
        self.imageLabel.setPixmap(pixmap)
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)

    def openZoomWindow(self, scaleFactor):
        self.zoomWindow = ZoomWindow(self.image, scaleFactor)
        self.zoomWindow.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
