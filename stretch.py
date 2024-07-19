import cv2
import numpy as np
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QImage, QPixmap


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1792, 1067)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.loadButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadButton.setGeometry(QtCore.QRect(320, 480, 151, 51))
        self.loadButton.setObjectName("loadButton")
        self.imageLabel = QtWidgets.QLabel(self.centralwidget)
        self.imageLabel.setGeometry(QtCore.QRect(100, 40, 640, 360))
        self.imageLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.imageLabel.setText("")
        self.imageLabel.setObjectName("imageLabel")
        self.contrastLabel = QtWidgets.QLabel(self.centralwidget)
        self.contrastLabel.setGeometry(QtCore.QRect(1080, 30, 640, 360))
        self.contrastLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.contrastLabel.setText("")
        self.contrastLabel.setObjectName("contrastLabel")
        self.contrastButton = QtWidgets.QPushButton(self.centralwidget)
        self.contrastButton.setGeometry(QtCore.QRect(1330, 470, 152, 51))
        self.contrastButton.setObjectName("contrastButton")
        self.stretchingLabel = QtWidgets.QLabel(self.centralwidget)
        self.stretchingLabel.setGeometry(QtCore.QRect(590, 470, 640, 360))
        self.stretchingLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.stretchingLabel.setText("")
        self.stretchingLabel.setObjectName("stretchingLabel")
        self.stretchButton = QtWidgets.QPushButton(self.centralwidget)
        self.stretchButton.setGeometry(QtCore.QRect(830, 890, 160, 60))
        self.stretchButton.setObjectName("stretchButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1792, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
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
        self.stretchButton.clicked.connect(self.contrastStretch)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loadButton.setText(_translate("MainWindow", "Load Image"))
        self.contrastButton.setText(_translate("MainWindow", "Contrast"))
        self.stretchButton.setText(_translate("MainWindow", "Contrast Stretching"))
        self.menuoperasi_titik.setTitle(_translate("MainWindow", "operasi titik"))
        self.actionContrast.setText(_translate("MainWindow", "Contrast"))

    def loadImage(self):
        self.image = cv2.imread('1311975.jpg')
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)  # Convert from BGR to RGB
        self.displayImage(1)

    def contrast(self):
        if self.image is None:
            print("Error: No image loaded.")
            return
        contrast = 1.8
        self.image = cv2.imread('1311975.jpg')
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

    def contrastStretch(self):
        if self.image is None:
            print("Error: No image loaded.")
            return
        self.image = cv2.imread('1311975.jpg')
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)  # Convert from BGR to RGB
        min_val = np.min(self.image)
        max_val = np.max(self.image)
        stretched_image = ((self.image - min_val) / (max_val - min_val) * 255).astype(np.uint8)
        self.displayImage(3, stretched_image)

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
            self.contrastLabel.setPixmap(pixmap)
            self.contrastLabel.setScaledContents(True)
            self.contrastLabel.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        elif windows == 3:
            self.stretchingLabel.setPixmap(pixmap)
            self.stretchingLabel.setScaledContents(True)
            self.stretchingLabel.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
