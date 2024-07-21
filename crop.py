import cv2
import numpy as np
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QImage, QPixmap


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.image = None

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(1415, 720)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.loadbutton = QtWidgets.QPushButton(self.centralwidget)
        self.loadbutton.setGeometry(QtCore.QRect(310, 460, 151, 51))
        self.loadbutton.setObjectName("loadbutton")
        self.imagelabel = QtWidgets.QLabel(self.centralwidget)
        self.imagelabel.setGeometry(QtCore.QRect(80, 20, 640, 360))
        self.imagelabel.setFrameShape(QtWidgets.QFrame.Box)
        self.imagelabel.setText("")
        self.imagelabel.setObjectName("imagelabel")
        self.resultlabel = QtWidgets.QLabel(self.centralwidget)
        self.resultlabel.setGeometry(QtCore.QRect(740, 20, 640, 360))
        self.resultlabel.setFrameShape(QtWidgets.QFrame.Box)
        self.resultlabel.setText("")
        self.resultlabel.setObjectName("resultlabel")
        self.resultbutton = QtWidgets.QPushButton(self.centralwidget)
        self.resultbutton.setGeometry(QtCore.QRect(990, 460, 152, 51))
        self.resultbutton.setObjectName("resultbutton")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1415, 24))
        self.menubar.setObjectName("menubar")
        self.menuoperasi_titik = QtWidgets.QMenu(self.menubar)
        self.menuoperasi_titik.setToolTipsVisible(True)
        self.menuoperasi_titik.setObjectName("menuoperasi_titik")
        self.menurotasi = QtWidgets.QMenu(self.menubar)
        self.menurotasi.setObjectName("menurotasi")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionMin45_Degree = QtWidgets.QAction(self)
        self.actionMin45_Degree.setObjectName("actionMin45_Degree")
        self.action45_Degree = QtWidgets.QAction(self)
        self.action45_Degree.setObjectName("action45_Degree")
        self.actionMin90_Degree = QtWidgets.QAction(self)
        self.actionMin90_Degree.setObjectName("actionMin90_Degree")
        self.action90_Degree = QtWidgets.QAction(self)
        self.action90_Degree.setObjectName("action90_Degree")
        self.action180_Degree = QtWidgets.QAction(self)
        self.action180_Degree.setObjectName("action180_Degree")
        self.menuoperasi_titik.addAction(self.actionMin45_Degree)
        self.menuoperasi_titik.addAction(self.action45_Degree)
        self.menuoperasi_titik.addAction(self.actionMin90_Degree)
        self.menuoperasi_titik.addAction(self.action90_Degree)
        self.menuoperasi_titik.addAction(self.action180_Degree)
        self.menubar.addAction(self.menuoperasi_titik.menuAction())
        self.menubar.addAction(self.menurotasi.menuAction())

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.loadbutton.clicked.connect(self.loadImage)
        self.resultbutton.clicked.connect(self.cropResult)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loadbutton.setText(_translate("MainWindow", "Load Image"))
        self.resultbutton.setText(_translate("MainWindow", "Result"))
        self.menuoperasi_titik.setTitle(_translate("MainWindow", "Rotasi"))
        self.menurotasi.setTitle(_translate("MainWindow", "rotasi"))
        self.actionMin45_Degree.setText(_translate("MainWindow", "-45 Degree"))
        self.action45_Degree.setText(_translate("MainWindow", "45 Degree"))
        self.actionMin90_Degree.setText(_translate("MainWindow", "-90 Degree"))
        self.action90_Degree.setText(_translate("MainWindow", "90 Degree"))
        self.action180_Degree.setText(_translate("MainWindow", "180 Degree"))

    def loadImage(self):
        self.image = cv2.imread('1311975.jpg')
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)  # Convert from BGR to RGB
        self.displayImage(1)

    def cropResult(self):
        if self.image is not None:
            # Prompt the user to enter width and height
            w, ok1 = QtWidgets.QInputDialog.getInt(self, "Input Width", "Enter crop width:", min=1, max=self.image.shape[1])
            h, ok2 = QtWidgets.QInputDialog.getInt(self, "Input Height", "Enter crop height:", min=1, max=self.image.shape[0])
            if ok1 and ok2:
                height, width, _ = self.image.shape
                # Calculate the starting point of the crop area (centered)
                start_x = max(0, (width - w) // 2)
                start_y = max(0, (height - h) // 2)
                end_x = start_x + w
                end_y = start_y + h
                cropped_image = self.image[start_y:end_y, start_x:end_x]
                self.displayImage(2, cropped_image)

    def displayImage(self, window=1, img=None):
        if img is None:
            img = self.image
        qformat = QImage.Format_RGB888
        if len(img.shape) == 3:
            if img.shape[2] == 4:
                qformat = QImage.Format_RGBA8888
        image = QImage(img, img.shape[1], img.shape[0], img.strides[0], qformat)
        pixmap = QPixmap.fromImage(image)
        if window == 1:
            self.imagelabel.setPixmap(pixmap)
            self.imagelabel.setScaledContents(True)
        elif window == 2:
            self.resultlabel.setPixmap(pixmap)
            self.resultlabel.setScaledContents(True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
