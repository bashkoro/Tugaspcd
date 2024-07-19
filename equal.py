# -*- coding: utf-8 -*-

import cv2
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from matplotlib import pyplot as plt

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1415, 720)
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
        self.resultlabel = QtWidgets.QLabel(self.centralwidget)
        self.resultlabel.setGeometry(QtCore.QRect(740, 20, 640, 360))
        self.resultlabel.setFrameShape(QtWidgets.QFrame.Box)
        self.resultlabel.setText("")
        self.resultlabel.setObjectName("resultlabel")
        self.resultbutton = QtWidgets.QPushButton(self.centralwidget)
        self.resultbutton.setGeometry(QtCore.QRect(990, 460, 152, 51))
        self.resultbutton.setObjectName("resultbutton")
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
        self.loadbutton.clicked.connect(self.loadImage)
        self.resultbutton.clicked.connect(self.equalizationResult)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loadbutton.setText(_translate("MainWindow", "Load Image"))
        self.resultbutton.setText(_translate("MainWindow", "Result"))
        self.menuoperasi_titik.setTitle(_translate("MainWindow", "operasi titik"))
        self.actionContrast.setText(_translate("MainWindow", "Contrast"))

    def loadImage(self):
        self.image = cv2.imread('1311975.jpg')
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)  # Convert from BGR to RGB
        self.displayImage(1)

    def equalizationResult(self):
        equalized_image = cv2.cvtColor(self.image, cv2.COLOR_RGB2YCrCb)
        equalized_image[:, :, 0] = cv2.equalizeHist(equalized_image[:, :, 0])
        equalized_image = cv2.cvtColor(equalized_image, cv2.COLOR_YCrCb2RGB)

        # Plot the RGB histograms
        colors = ('r', 'g', 'b')
        plt.figure(figsize=(10, 4))

        for i, color in enumerate(colors):
            plt.subplot(1, 2, 1)
            plt.hist(self.image[:, :, i].ravel(), 256, [0, 256], color=color, alpha=0.5)
            plt.title('Original Histogram')
            plt.xlabel('Intensity Value')
            plt.ylabel('Pixel Count')

        for i, color in enumerate(colors):
            plt.subplot(1, 2, 2)
            plt.hist(equalized_image[:, :, i].ravel(), 256, [0, 256], color=color, alpha=0.5)
            plt.title('Equalized Histogram')
            plt.xlabel('Intensity Value')
            plt.ylabel('Pixel Count')

        plt.tight_layout()
        plt.show()

        self.displayImage(2, equalized_image)  # Display the result in the result label

    def displayImage(self, windows=1, img=None):
        if img is None:
            img = self.image

        qformat = QImage.Format_Indexed8
        if len(img.shape) == 3:  # RGB or RGBA image
            if img.shape[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        elif len(img.shape) == 2:  # Grayscale image
            qformat = QImage.Format_Grayscale8

        image = QImage(img, img.shape[1], img.shape[0], img.strides[0], qformat)
        pixmap = QPixmap.fromImage(image)

        if windows == 1:
            self.citralabel.setPixmap(pixmap)
            self.citralabel.setScaledContents(True)
            self.citralabel.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        elif windows == 2:
            self.resultlabel.setPixmap(pixmap)
            self.resultlabel.setScaledContents(True)
            self.resultlabel.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
