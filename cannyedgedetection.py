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
        self.loadbutton_2.clicked.connect(self.cannyedgedetection)

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

    def cannyedgedetection(self):
        import cv2
        import numpy as np

        # Load the image
        img = cv2.imread('1311975.jpg')

        # Convert the image to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Apply Canny edge detection
        edges = cv2.Canny(gray, 100, 200)

        # Display the result
        cv2.imshow('Canny Edge Detection', edges)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        # Langkah 1: Reduksi Noise
        # def gaussian_filter(img, sigma=1.4):
        #     kernel = np.array([[1, 3, 5, 3, 1],
        #                        [3, 5, 7, 5, 3],
        #                        [5, 7, 9, 7, 5],
        #                        [3, 5, 7, 5, 3],
        #                        [1, 3, 5, 3, 1]]) * (1.0 / 57)
        #     filtered_img = cv2.filter2D(img, -1, kernel)
        #     return filtered_img
        #
        # # Langkah 2: Finding Gradian
        # def calculate_gradient(img):
        #     dy, dx = np.gradient(img)
        #     gradient_magnitude = np.sqrt(dx ** 2 + dy ** 2)
        #     gradient_direction = np.arctan2(dy, dx)
        #     return gradient_magnitude, gradient_direction
        #
        # # Langkah 3: Non-Maximum Suppression
        # def non_maximum_suppression(gradient_magnitude, gradient_direction):
        #     """Performs non-maximum suppression to thin out the edges."""
        #     H, W = gradient_magnitude.shape
        #     output = np.zeros((H, W), dtype=np.int32)
        #
        #     for i in range(1, H - 1):
        #         for j in range(1, W - 1):
        #             angle = gradient_direction[i, j] * 180. / np.pi
        #             angle = (angle + 180) % 180
        #
        #             if (0 <= angle < 22.5) or (157.5 <= angle <= 180):
        #                 q = gradient_magnitude[i, (j - 1) % W]
        #                 r = gradient_magnitude[i, (j + 1) % W]
        #             elif (22.5 <= angle < 67.5):
        #                 q = gradient_magnitude[(i - 1) % H, (j + 1) % W]
        #                 r = gradient_magnitude[(i + 1) % H, (j - 1) % W]
        #             elif (67.5 <= angle < 112.5):
        #                 q = gradient_magnitude[(i - 1) % H, j]
        #                 r = gradient_magnitude[(i + 1) % H, j]
        #             elif (112.5 <= angle < 157.5):
        #                 q = gradient_magnitude[(i + 1) % H, (j + 1) % W]
        #                 r = gradient_magnitude[(i - 1) % H, (j - 1) % W]
        #
        #             if (gradient_magnitude[i, j] >= q) and (gradient_magnitude[i, j] >= r):
        #                 output[i, j] = gradient_magnitude[i, j]
        #             else:
        #                 output[i, j] = 0
        #
        #     return output
        #
        # # Langkah 4: Hysteresis Thresholding
        # def hysteresis_thresholding(non_maximum_suppressed, low_threshold=0, high_threshold=0):
        #     H, W = non_maximum_suppressed.shape
        #     output = np.zeros((H, W), dtype=np.uint8)
        #
        #     weak = np.int32(25)
        #     strong = np.int32(255)
        #
        #     strong_i, strong_j = np.where(non_maximum_suppressed >= high_threshold)
        #     zeros_i, zeros_j = np.where(non_maximum_suppressed < low_threshold)
        #
        #     weak_i, weak_j = np.where(
        #         (non_maximum_suppressed >= low_threshold) & (non_maximum_suppressed < high_threshold))
        #
        #     output[strong_i, strong_j] = strong
        #     output[weak_i, weak_j] = weak
        #
        #     return output
        #
        # # Contoh penggunaan
        # img = cv2.imread('1311975.jpg', cv2.IMREAD_GRAYSCALE)
        # filtered_img = gaussian_filter(img)
        # gradient_magnitude, gradient_direction = calculate_gradient(filtered_img)
        # non_maximum_suppressed = non_maximum_suppression(gradient_magnitude, gradient_direction)
        # edge_img = hysteresis_thresholding(non_maximum_suppressed, low_threshold=50, high_threshold=100)
        #
        # cv2.imshow('Edge Detection', edge_img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
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
