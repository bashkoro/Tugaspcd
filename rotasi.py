import cv2
import numpy as np
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QImage, QPixmap


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1736, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.imageLabel = QtWidgets.QLabel(self.centralwidget)
        self.imageLabel.setGeometry(QtCore.QRect(60, 10, 720, 480))
        self.imageLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.imageLabel.setText("")
        self.imageLabel.setObjectName("imageLabel")
        self.resultLabel = QtWidgets.QLabel(self.centralwidget)
        self.resultLabel.setGeometry(QtCore.QRect(960, 10, 720, 480))
        self.resultLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.resultLabel.setText("")
        self.resultLabel.setObjectName("resultLabel")
        self.imageButton = QtWidgets.QPushButton(self.centralwidget)
        self.imageButton.setGeometry(QtCore.QRect(270, 530, 200, 75))
        self.imageButton.setObjectName("imageButton")
        self.resultButton = QtWidgets.QPushButton(self.centralwidget)
        self.resultButton.setGeometry(QtCore.QRect(1220, 530, 200, 75))
        self.resultButton.setObjectName("resultButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1736, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.imageButton.clicked.connect(self.loadImage)
        self.resultButton.clicked.connect(self.rotateImage)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.imageButton.setText(_translate("MainWindow", "Load Image"))
        self.resultButton.setText(_translate("MainWindow", "Rotate Image"))

    def loadImage(self):
        self.image = cv2.imread('1311975.jpg')
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        self.displayImage(1)

    def rotateImage(self):
        degree = 180  # You can change this value to set the desired rotation degree
        self.rotationResult(degree)

    def rotationResult(self, degree):
        if self.image is None:
            print("Error: No image loaded.")
            return
        h, w = self.image.shape[:2]
        rotationMatrix = cv2.getRotationMatrix2D((w / 2, h / 2), degree, 1)
        nW = int((h * np.abs(rotationMatrix[0, 1])) + (w * np.abs(rotationMatrix[0, 0])))
        nH = int((h * np.abs(rotationMatrix[0, 0])) + (w * np.abs(rotationMatrix[0, 1])))
        rotationMatrix[0, 2] += (nW / 2) - (w / 2)
        rotationMatrix[1, 2] += (nH / 2) - (h / 2)
        rotated_image = cv2.warpAffine(self.image, rotationMatrix, (nW, nH))
        self.displayImage(2, rotated_image)

    def displayImage(self, window=1, img=None):
        if img is None:
            img = self.image
        qformat = QImage.Format_Indexed8
        if len(img.shape) == 3:
            if img.shape[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        elif len(img.shape) == 2:
            qformat = QImage.Format_Grayscale8

        image = QImage(img, img.shape[1], img.shape[0], img.strides[0], qformat)
        pixmap = QPixmap.fromImage(image)

        if window == 1:
            self.imageLabel.setPixmap(pixmap)
            self.imageLabel.setScaledContents(True)
            self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        elif window == 2:
            self.resultLabel.setPixmap(pixmap)
            self.resultLabel.setScaledContents(True)
            self.resultLabel.setAlignment(QtCore.Qt.AlignCenter)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
