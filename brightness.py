import cv2
import numpy as np
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QImage, QPixmap


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.loadbutton = QtWidgets.QPushButton(self.centralwidget)
        self.loadbutton.setGeometry(QtCore.QRect(310, 460, 151, 51))
        self.loadbutton.setObjectName("loadbutton")
        self.citralabel = QtWidgets.QLabel(self.centralwidget)
        self.citralabel.setGeometry(QtCore.QRect(80, 20, 640, 360))
        self.citralabel.setFrameShape(QtWidgets.QFrame.Box)
        self.citralabel.setText("")
        self.citralabel.setObjectName("citralabel")
        self.graylabel = QtWidgets.QLabel(self.centralwidget)
        self.graylabel.setGeometry(QtCore.QRect(740, 20, 640, 360))
        self.graylabel.setFrameShape(QtWidgets.QFrame.Box)
        self.graylabel.setText("")
        self.graylabel.setObjectName("graylabel")
        self.brightbutton = QtWidgets.QPushButton(self.centralwidget)
        self.brightbutton.setGeometry(QtCore.QRect(990, 460, 152, 51))
        self.brightbutton.setObjectName("brightbutton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.loadbutton.clicked.connect(self.loadImage)
        self.brightbutton.clicked.connect(self.brightness)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loadbutton.setText(_translate("MainWindow", "Load Image"))
        self.brightbutton.setText(_translate("MainWindow", "Brightness"))

    def loadImage(self):
        self.image = cv2.imread('1311975.jpg')
        if self.image is None:
            print("Error: Image not found or unable to load.")
            return
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        self.displayImage(1)

    def brightness(self):
        if self.image is None:
            print("Error: No image loaded.")
            return
        bright = 50
        bright_image = cv2.convertScaleAbs(self.image, alpha=1, beta=bright)
        self.displayImage(2, bright_image)

    def displayImage(self, windows=1, img=None):
        if img is None:
            img = self.image

        qformat = QImage.Format_Indexed8
        if len(img.shape) == 3:  # RGB or RGBA image
            if img.shape[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888

        image = QImage(img, img.shape[1], img.shape[0], img.strides[0], qformat)
        pixmap = QPixmap.fromImage(image)

        if windows == 1:
            self.citralabel.setPixmap(pixmap)
            self.citralabel.setScaledContents(True)
            self.citralabel.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        elif windows == 2:
            self.graylabel.setPixmap(pixmap)
            self.graylabel.setScaledContents(True)
            self.graylabel.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
