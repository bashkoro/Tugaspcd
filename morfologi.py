import cv2
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.loadbutton = QtWidgets.QPushButton(self.centralwidget)
        self.loadbutton.setGeometry(QtCore.QRect(310, 400, 151, 51))
        self.loadbutton.setObjectName("loadbutton")
        self.imglabel = QtWidgets.QLabel(self.centralwidget)
        self.imglabel.setGeometry(QtCore.QRect(67, 25, 640, 360))
        self.imglabel.setFrameShape(QtWidgets.QFrame.Box)
        self.imglabel.setText("")
        self.imglabel.setObjectName("imglabel")
        self.loadbutton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.loadbutton_2.setGeometry(QtCore.QRect(310, 460, 151, 51))
        self.loadbutton_2.setObjectName("loadbutton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.loadbutton.clicked.connect(self.loadImage)
        self.loadbutton_2.clicked.connect(self.morfologi)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loadbutton.setText(_translate("MainWindow", "Load Image"))
        self.loadbutton_2.setText(_translate("MainWindow", "FIlter"))

    def loadImage(self):
        self.image = cv2.imread('1311975.jpg')
        if self.image is None:
            QtWidgets.QMessageBox.critical(None, 'Error', 'Failed to load image.')
            return
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)  # Convert from BGR to RGB
        self.displayImage()

    def morfologi(self):
        # 1. Convert image to grayscale and apply binary thresholding
        image = cv2.imread('1311975.jpg')
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        thresh, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

        # Display the menu
        print("Select the operation:")
        print("1. Morphological Opening")
        print("2. Erosion")
        print("3. Dilation")
        print("4. Morphological Closing")
        print("5. Exit")

        while True:
            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                # Perform opening using cv2.MORPH_OPEN
                kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
                morph_open = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
                cv2.imshow('Morphological Opening', morph_open)
            elif choice == '2':
                # Perform erosion using cv2.erode
                kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
                eroded = cv2.erode(binary, kernel, iterations=1)
                cv2.imshow('Erosion', eroded)
            elif choice == '3':
                # Perform dilation using cv2.dilate
                kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
                dilated = cv2.dilate(binary, kernel, iterations=1)
                cv2.imshow('Dilation', dilated)
            elif choice == '4':
                # Perform closing using cv2.MORPH_CLOSE
                kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
                morph_close = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
                cv2.imshow('Morphological Closing', morph_close)
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

            cv2.waitKey(0)

    def displayImage(self):
        qformat = QImage.Format_RGB888
        image = QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.strides[0], qformat)
        pixmap = QPixmap.fromImage(image)
        self.imglabel.setPixmap(pixmap)
        self.imglabel.setScaledContents(True)
        self.imglabel.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
