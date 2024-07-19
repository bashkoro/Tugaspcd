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

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1415, 24))
        self.menubar.setObjectName("menubar")

        self.menuoperasi_titik = QtWidgets.QMenu(self.menubar)
        self.menuoperasi_titik.setObjectName("menuoperasi_titik")

        MainWindow.setMenuBar(self.menubar)

        self.actionMin45_Degree = QtWidgets.QAction(MainWindow)
        self.actionMin45_Degree.setObjectName("actionMin45_Degree")
        self.menuoperasi_titik.addAction(self.actionMin45_Degree)

        self.action45_Degree = QtWidgets.QAction(MainWindow)
        self.action45_Degree.setObjectName("action45_Degree")
        self.menuoperasi_titik.addAction(self.action45_Degree)

        self.actionMin90_Degree = QtWidgets.QAction(MainWindow)
        self.actionMin90_Degree.setObjectName("actionMin90_Degree")
        self.menuoperasi_titik.addAction(self.actionMin90_Degree)

        self.action90_Degree = QtWidgets.QAction(MainWindow)
        self.action90_Degree.setObjectName("action90_Degree")
        self.menuoperasi_titik.addAction(self.action90_Degree)

        self.action180_Degree = QtWidgets.QAction(MainWindow)
        self.action180_Degree.setObjectName("action180_Degree")
        self.menuoperasi_titik.addAction(self.action180_Degree)

        self.menubar.addAction(self.menuoperasi_titik.menuAction())

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.loadbutton.clicked.connect(self.loadImage)
        self.resultbutton.clicked.connect(self.rotationResult)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loadbutton.setText(_translate("MainWindow", "Load Image"))
        self.resultbutton.setText(_translate("MainWindow", "Rotation"))
        self.menuoperasi_titik.setTitle(_translate("MainWindow", "Rotasi"))
        self.actionMin45_Degree.setText(_translate("MainWindow", "-45 Degree"))
        self.action45_Degree.setText(_translate("MainWindow", "45 Degree"))
        self.actionMin90_Degree.setText(_translate("MainWindow", "-90 Degree"))
        self.action90_Degree.setText(_translate("MainWindow", "90 Degree"))
        self.action180_Degree.setText(_translate("MainWindow", "180 Degree"))

    def loadImage(self):
        self.image = cv2.imread('1311975.jpg')
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)  # Convert from BGR to RGB
        self.displayImage(1)

    def rotationResult(self, degree):
        h, w = self.image.shape[:2]
        rotationMatrix = cv2.getRotationMatrix2D((w / 2, h / 2), degree, 1)
        cos = np.abs(rotationMatrix[0, 0])
        sin = np.abs(rotationMatrix[0, 1])
        nW = int((h * sin) + (w * cos))
        nH = int((h * cos) + (w * sin))
        rotationMatrix[0, 2] += (nW / 2) - w / 2
        rotationMatrix[1, 2] += (nH / 2) - h / 2
        rot_image = cv2.warpAffine(self.image, rotationMatrix, (nW, nH))
        self.image = rot_image
        self.displayImage(2)

    def displayImage(self, windows=1, img=None):
        if img is None:
            img = self.image
        qformat = QImage.Format_RGB888
        if len(img.shape) == 3:
            if img.shape[2] == 4:
                qformat = QImage.Format_RGBA8888
        image = QImage(img, img.shape[1], img.shape[0], img.strides[0], qformat)
        pixmap = QPixmap.fromImage(image)
        if windows == 1:
            self.citralabel.setPixmap(pixmap)
            self.citralabel.setScaledContents(True)
        elif windows == 2:
            self.resultlabel.setPixmap(pixmap)
            self.resultlabel.setScaledContents(True)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
