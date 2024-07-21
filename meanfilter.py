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
        self.loadbutton_2.clicked.connect(self.meanfilter)

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

    def meanfilter(self):
        image = cv2.imread('1311975.jpg')

        # Define a 3x3 mean filter kernel
        kernel_size = 6
        mean_kernel = np.array([[1 / 36, 1 / 36, 1 / 36, 1 / 36, 1 / 36, 1 / 36],
                                [1 / 36, 1 / 36, 1 / 36, 1 / 36, 1 / 36, 1 / 36],
                                [1 / 36, 1 / 36, 1 / 36, 1 / 36, 1 / 36, 1 / 36],
                                [1 / 36, 1 / 36, 1 / 36, 1 / 36, 1 / 36, 1 / 36],
                                [1 / 36, 1 / 36, 1 / 36, 1 / 36, 1 / 36, 1 / 36],
                                [1 / 36, 1 / 36, 1 / 36, 1 / 36, 1 / 36, 1 / 36]], dtype=np.float32)

        # Apply the mean filter
        mean_filtered_image = cv2.filter2D(image, -1, mean_kernel)

        # Display and save the result
        cv2.imshow('Mean Filtered Image', mean_filtered_image)
        cv2.imwrite('path/to/save/mean_filtered_image.jpg', mean_filtered_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

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
