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
        self.loadbutton_2.clicked.connect(self.edgedetection)

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

    def edgedetection(self):
        image = cv2.imread('1311975.jpg')
        # Konversi gambar ke grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

        # Inisialisasi kernel Sobel untuk sumbu x dan y
        kernel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
        kernel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

        # Konvolusi gambar dengan kernel Sobel untuk sumbu x dan y
        grad_x = cv2.filter2D(gray, cv2.CV_32F, kernel_x)
        grad_y = cv2.filter2D(gray, cv2.CV_32F, kernel_y)

        # Hitung magnitude gradien
        grad = np.sqrt(grad_x ** 2 + grad_y ** 2)

        # Normalisasi gradient dalam range 0-255
        grad_norm = (grad - np.min(grad)) / (np.max(grad) - np.min(grad)) * 255
        grad_norm = grad_norm.astype(np.uint8)

        # Tampilkan hasil edge detection
        cv2.imshow('Edge Detection', grad_norm)
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
