import cv2
import numpy as np
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets


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
        self.citralabel2 = QtWidgets.QLabel(self.centralwidget)
        self.citralabel2.setGeometry(QtCore.QRect(740, 20, 640, 360))
        self.citralabel.setFrameShape(QtWidgets.QFrame.Box)
        self.citralabel2.setText("")
        self.citralabel2.setObjectName("citralabel2")
        self.loadbutton2 = QtWidgets.QPushButton(self.centralwidget)
        self.loadbutton2.setGeometry(QtCore.QRect(990, 460, 152, 51))
        self.loadbutton2.setObjectName("loadbutton2")
        self.aritmethicButton = QtWidgets.QPushButton(self.centralwidget)
        self.aritmethicButton.setGeometry(QtCore.QRect(310, 550, 151, 51))
        self.aritmethicButton.setObjectName("aritmethicButton")
        self.aritmethicButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.aritmethicButton_2.setGeometry(QtCore.QRect(490, 550, 151, 51))
        self.aritmethicButton_2.setObjectName("aritmethicButton_2")
        self.aritmethicButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.aritmethicButton_3.setGeometry(QtCore.QRect(660, 550, 151, 51))
        self.aritmethicButton_3.setObjectName("aritmethicButton_3")
        self.aritmethicButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.aritmethicButton_4.setGeometry(QtCore.QRect(840, 550, 151, 51))
        self.aritmethicButton_4.setObjectName("aritmethicButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1415, 24))
        self.menubar.setObjectName("menubar")
        self.menuoperasi_titik = QtWidgets.QMenu(self.menubar)
        self.menuoperasi_titik.setToolTipsVisible(True)
        self.menuoperasi_titik.setObjectName("menuoperasi_titik")
        self.menurotasi = QtWidgets.QMenu(self.menubar)
        self.menurotasi.setObjectName("menurotasi")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionMin45_Degree = QtWidgets.QAction(MainWindow)
        self.actionMin45_Degree.setObjectName("actionMin45_Degree")
        self.action45_Degree = QtWidgets.QAction(MainWindow)
        self.action45_Degree.setObjectName("action45_Degree")
        self.actionMin90_Degree = QtWidgets.QAction(MainWindow)
        self.actionMin90_Degree.setObjectName("actionMin90_Degree")
        self.action90_Degree = QtWidgets.QAction(MainWindow)
        self.action90_Degree.setObjectName("action90_Degree")
        self.action180_Degree = QtWidgets.QAction(MainWindow)
        self.action180_Degree.setObjectName("action180_Degree")
        self.menuoperasi_titik.addAction(self.actionMin45_Degree)
        self.menuoperasi_titik.addAction(self.action45_Degree)
        self.menuoperasi_titik.addAction(self.actionMin90_Degree)
        self.menuoperasi_titik.addAction(self.action90_Degree)
        self.menuoperasi_titik.addAction(self.action180_Degree)
        self.menubar.addAction(self.menuoperasi_titik.menuAction())
        self.menubar.addAction(self.menurotasi.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.loadbutton.clicked.connect(self.loadImage)
        self.loadbutton2.clicked.connect(self.loadImage2)
        self.aritmethicButton.clicked.connect(self.addResult)
        self.aritmethicButton_2.clicked.connect(self.subtractResult)
        self.aritmethicButton_3.clicked.connect(self.divideResult)
        self.aritmethicButton_4.clicked.connect(self.multipleResult)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loadbutton.setText(_translate("MainWindow", "Load Image"))
        self.loadbutton2.setText(_translate("MainWindow", "Load Image 2"))
        self.aritmethicButton.setText(_translate("MainWindow", "Add"))
        self.aritmethicButton_2.setText(_translate("MainWindow", "Substract"))
        self.aritmethicButton_3.setText(_translate("MainWindow", "Divide"))
        self.aritmethicButton_4.setText(_translate("MainWindow", "Multiple"))
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
    def loadImage2(self):
        self.image = cv2.imread('1315490.jpg')
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)  # Convert from BGR to RGB
        self.displayImage(2)

    def addResult(self):

        # Load two images
        image1 = cv2.imread('1311975.jpg')
        image2 = cv2.imread('1315490.jpg')

        # Ensure the images are of the same size
        image1 = cv2.resize(image1, (300, 300))
        image2 = cv2.resize(image2, (300, 300))

        # Perform image addition
        added_image = cv2.add(image1, image2)

        # Display and save the result
        cv2.imshow('Added Image', added_image)
        cv2.imwrite('path/to/save/added_image.jpg', added_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def subtractResult(self):
        image1 = cv2.imread('1311975.jpg')
        image2 = cv2.imread('1315490.jpg')

        # Ensure the images are of the same size
        image1 = cv2.resize(image1, (300, 300))
        image2 = cv2.resize(image2, (300, 300))

        # Perform image subtraction
        subtracted_image = cv2.subtract(image1, image2)

        # Display and save the result
        cv2.imshow('Subtracted Image', subtracted_image)
        cv2.imwrite('path/to/save/subtracted_image.jpg', subtracted_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def divideResult(self):
        image1 = cv2.imread('1311975.jpg')
        image2 = cv2.imread('1315490.jpg')

        image1 = cv2.resize(image1, (300, 300))
        image2 = cv2.resize(image2, (300, 300))

        # Convert images to float to avoid overflow
        image1 = np.float32(image1)
        image2 = np.float32(image2)

        # Perform image division
        divided_image = cv2.divide(image1, image2)

        # Convert back to uint8
        divided_image = np.uint8(np.clip(divided_image, 0, 255))

        # Display and save the result
        cv2.imshow('Divided Image', divided_image)
        cv2.imwrite('path/to/save/divided_image.jpg', divided_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def multipleResult(self):
        image1 = cv2.imread('1311975.jpg')
        image2 = cv2.imread('1315490.jpg')
        image1 = cv2.resize(image1, (300, 300))
        image2 = cv2.resize(image2, (300, 300))
        # Convert images to float to avoid overflow
        image1 = np.float32(image1)
        image2 = np.float32(image2)

        # Perform image multiplication
        multiplied_image = cv2.multiply(image1, image2)

        # Convert back to uint8
        multiplied_image = np.uint8(np.clip(multiplied_image, 0, 255))

        # Display and save the result
        cv2.imshow('Multiplied Image', multiplied_image)
        cv2.imwrite('path/to/save/multiplied_image.jpg', multiplied_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

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
            self.citralabel2.setPixmap(pixmap)
            self.citralabel2.setScaledContents(True)
            self.citralabel2.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
