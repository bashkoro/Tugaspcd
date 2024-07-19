import cv2
import numpy as np
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QImage, QPixmap

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
        self.contrastLabel = QtWidgets.QLabel(self.centralwidget)
        self.contrastLabel.setGeometry(QtCore.QRect(740, 20, 640, 360))
        self.contrastLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.contrastLabel.setText("")
        self.contrastLabel.setObjectName("contrastLabel")
        self.contrastButton = QtWidgets.QPushButton(self.centralwidget)
        self.contrastButton.setGeometry(QtCore.QRect(990, 460, 152, 51))
        self.contrastButton.setObjectName("contrastButton")
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
        self.contrastButton.clicked.connect(self.contrast)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loadButton.setText(_translate("MainWindow", "Load Image"))
        self.contrastButton.setText(_translate("MainWindow", "Contrast"))
        self.menuoperasi_titik.setTitle(_translate("MainWindow", "operasi titik"))
        self.actionContrast.setText(_translate("MainWindow", "Contrast"))

    def loadImage(self):
        self.image = cv2.imread('1311975.jpg')
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)  # Convert from BGR to RGB
        self.displayImage(1)

    def contrast(self):
        self.image = cv2.imread('1311975.jpg')
        contrast = 1.8
        H, W = self.image.shape[:2]
        for i in np.arange(H):
            for j in np.arange(W):
                for k in range(3):
                    a = self.image[i, j, k]
                    b = a * contrast
                    if b > 255:
                        b = 255
                    elif b < 0:
                        b = 0
                    self.image[i, j, k] = b
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)  # Convert from BGR to RGB
        self.displayImage(2)

    def displayImage(self, windows=1):
        qformat = QImage.Format_Indexed8
        if len(self.image.shape) == 3:
            if self.image.shape[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        if windows == 1:
            img = QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.strides[0], qformat)
            pixmap = QPixmap.fromImage(img)

            # Set the pixmap to the label
            self.imageLabel.setPixmap(pixmap)
            # Scale the pixmap to fit the label
            self.imageLabel.setScaledContents(True)
            # Align the label contents to center
            self.imageLabel.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        if windows == 2:
            img = QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.strides[0], qformat)
            pixmap = QPixmap.fromImage(img)
            self.contrastLabel.setPixmap(pixmap)
            # Scale the pixmap to fit the label
            self.contrastLabel.setScaledContents(True)
            # Align the label contents to center
            self.contrastLabel.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
