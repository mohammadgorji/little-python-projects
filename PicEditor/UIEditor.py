import random
import sys
import cv2
import imutils
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from PySide2.QtGui import QPixmap, QImage
from MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.filename = None
        self.tmp = None
        self.brightness_value_now = 0
        self.blur_value_now = 0

        self.pushButton.clicked.connect(self.savePhoto)
        self.pushButton_2.clicked.connect(self.loadImage)
        self.verticalSlider.valueChanged['int'].connect(self.brightness_value)
        self.verticalSlider_2.valueChanged['int'].connect(self.blur_value)

    def loadImage(self):
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        self.image = cv2.imread(self.filename)
        self.setPhoto(self.image)

    def savePhoto(self):
        cv2.imwrite(self.filename, self.tmp)

    def setPhoto(self, image):
        self.temp = image
        image = imutils.resize(image, width=640)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(
            frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.label.setPixmap(QPixmap.fromImage(image))

    def brightness_value(self, value):
        self.brightness_value_now = value
        self.update()

    def blur_value(self, value):
        self.blur_value_now = value
        self.update()

    def changeBrightness(self, img, value):
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)
        lim = 255 - value
        v[v > lim] = 255
        v[v <= lim] += value
        final_hsv = cv2.merge((h, s, v))
        img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
        return img

    def changeBlur(self, img, value):
        kernel_size = (value+1, value+1)
        img = cv2.blur(img, kernel_size)
        return img

    def update(self):
        img = self.changeBrightness(self.image, self.brightness_value_now)
        img = self.changeBlur(img, self.blur_value_now)
        self.setPhoto(img)


app = QApplication(sys.argv)
w = MainWindow()
app.exec_()
