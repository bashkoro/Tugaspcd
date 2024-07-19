import cv2
import numpy as np
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1415, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.loadButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadButton.setGeometry(QtCore.QRect(310, 460, 151, 51))
        self.loadButton.setObjectName("loadButton")
        self.imageLabel = QtWidgets.QLabel(self.centralwidget)
        self.imageLabel.setGeometry(QtCore.QRect(80, 20, 640, 360))
        self.imageLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.imageLabel.setText("")
        self.imageLabel.setObjectName("imageLabel")
        self.binaryLabel = QtWidgets.QLabel(self.centralwidget)
        self.binaryLabel.setGeometry(QtCore.QRect(740, 20, 640, 360))
        self.binaryLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.binaryLabel.setText("")
        self.binaryLabel.setObjectName("binaryLabel")
        self.binaryButton = QtWidgets.QPushButton(self.centralwidget)
        self.binaryButton.setGeometry(QtCore.QRect(990, 460, 152, 51))
        self.binaryButton.setObjectName("binaryButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1415, 24))
        self.menubar.setObjectName("menubar")
        self.menuoperasi_titik = QtWidgets.QMenu(self.menubar)
        self.menuoperasi_titik.setObjectName("menuoperasi_titik")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionContrast = QtWidgets.QAction(MainWindow)
        self.actionContrast.setObjectName("actionContrast")
        self.menuoperasi_titik.addAction(self.actionContrast)
        self.menubar.addAction(self.menuoperasi_titik.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.loadButton.clicked.connect(self.loadImage)
        self.binaryButton.clicked.connect(self.binaryImage)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loadButton.setText(_translate("MainWindow", "Load Image"))
        self.binaryButton.setText(_translate("MainWindow", "Binary Image"))
        self.menuoperasi_titik.setTitle(_translate("MainWindow", "operasi titik"))
        self.actionContrast.setText(_translate("MainWindow", "Contrast"))

    def loadImage(self):
        self.image = cv2.imread('1311975.jpg')
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)  # Convert from BGR to RGB
        self.displayImage(1)

    def binaryImage(self):
        self.image = cv2.imread('1311975.jpg')
        gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
        _, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)  # Apply binary threshold
        self.displayImage(2, binary_image)

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
            self.imageLabel.setPixmap(pixmap)
            self.imageLabel.setScaledContents(True)
            self.imageLabel.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        elif windows == 2:
            self.binaryLabel.setPixmap(pixmap)
            self.binaryLabel.setScaledContents(True)
            self.binaryLabel.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
