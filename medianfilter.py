import cv2
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from scipy.ndimage import median_filter




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
        self.loadbutton_2.clicked.connect(self.medianfilter)

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

    def medianfilter(self):
        image = cv2.imread('1311975.jpg')

        # Define the custom array (e.g., a 3x3 matrix)
        custom_array = np.array([[1, 1, 1],
                                 [1, 0, 1],
                                 [1, 1, 1]], dtype=np.float32)

        # Convert image to grayscale for simplicity
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Pad the image to apply the custom array
        pad_size = custom_array.shape[0] // 2
        padded_image = np.pad(gray_image, pad_size, mode='constant', constant_values=0)

        # Apply the custom array (element-wise addition)
        modified_image = padded_image.copy()
        for i in range(pad_size, gray_image.shape[0] + pad_size):
            for j in range(pad_size, gray_image.shape[1] + pad_size):
                region = padded_image[i - pad_size:i + pad_size + 1, j - pad_size:j + pad_size + 1]
                modified_image[i, j] = np.sum(region * custom_array)

        # Apply the median filter
        median_filtered_image = median_filter(modified_image, size=custom_array.shape[0])

        # Convert back to BGR if the original image was in color
        median_filtered_image_color = cv2.cvtColor(median_filtered_image, cv2.COLOR_GRAY2BGR)

        # Display and save the result
        cv2.imshow('Custom Median Filtered Image', median_filtered_image_color)
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
