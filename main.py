from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Online whiteboard')

        self.setGeometry(100, 100, 800, 900)

        self.image = QImage(self.size(), QImage.Format_ARGB32)

        self.color = Qt.white

        self.image.fill(Qt.white)

        self.drawing = False
        self.brushSize = 2
        self.brushColor = Qt.black

        self.lastPoint = QPoint()

        main_menu = self.menuBar()

        file_menu = main_menu.addMenu("File")

        b_size = main_menu.addMenu("Brush Size")

        b_color = main_menu.addMenu("Brush Color")

        b_erase = main_menu.addMenu("Eraser")

        b_back = main_menu.addMenu("Fill color")

        save_action = QAction("Save", self)
        save_action.setShortcut("Ctrl + S")
        file_menu.addAction(save_action)
        save_action.triggered.connect(self.save)

        clear_action = QAction("Clear", self)
        clear_action.setShortcut("Ctrl + C")
        file_menu.addAction(clear_action)
        clear_action.triggered.connect(self.clear)

        erase_action = QAction("Eraser", self)
        b_erase.addAction(erase_action)
        erase_action.triggered.connect(self.erase)

        fill_action = QAction("Blue", self)
        self.color = Qt.blue
        b_back.addAction(fill_action)
        fill_action.triggered.connect(self.fill_blue)

        fill_action = QAction("Red", self)
        self.color = Qt.red
        b_back.addAction(fill_action)
        fill_action.triggered.connect(self.fill_red)

        fill_action = QAction("Green", self)
        self.color = Qt.green
        b_back.addAction(fill_action)
        fill_action.triggered.connect(self.fill_green)

        fill_action = QAction("Black", self)
        self.color = Qt.black
        b_back.addAction(fill_action)
        fill_action.triggered.connect(self.fill_black)

        fill_action = QAction("Yellow", self)
        self.color = Qt.yellow
        b_back.addAction(fill_action)
        fill_action.triggered.connect(self.fill_yellow)

        fill_action = QAction("White", self)
        self.color = Qt.white
        b_back.addAction(fill_action)
        fill_action.triggered.connect(self.fill_white)

        pix_4 = QAction("4px", self)
        b_size.addAction(pix_4)
        pix_4.triggered.connect(self.pixel_4)

        pix_7 = QAction("7px", self)
        b_size.addAction(pix_7)
        pix_7.triggered.connect(self.pixel_7)

        pix_9 = QAction("9px", self)
        b_size.addAction(pix_9)
        pix_9.triggered.connect(self.pixel_9)

        pix_12 = QAction("12px", self)
        b_size.addAction(pix_12)
        pix_12.triggered.connect(self.pixel_12)

        pix_15 = QAction("15px", self)
        b_size.addAction(pix_15)
        pix_15.triggered.connect(self.pixel_15)

        black = QAction("Black", self)
        b_color.addAction(black)
        black.triggered.connect(self.black_color)

        green = QAction("Green", self)
        b_color.addAction(green)
        green.triggered.connect(self.green_color)

        yellow = QAction("Yellow", self)
        b_color.addAction(yellow)
        yellow.triggered.connect(self.yellow_color)

        red = QAction("Red", self)
        b_color.addAction(red)
        red.triggered.connect(self.red_color)

        blue = QAction("Blue", self)
        b_color.addAction(blue)
        blue.triggered.connect(self.blue_color)

        blue = QAction("White", self)
        b_color.addAction(blue)
        blue.triggered.connect(self.white_color)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()

    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)

            painter.setPen(QPen(self.brushColor, self.brushSize,
                                Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))

            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False

    def paintEvent(self, event):
        canvas_painter = QPainter(self)
        canvas_painter.drawImage(self.rect(), self.image, self.image.rect())

    def save(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")

        if file_path == "":
            return
        self.image.save(file_path)

    def clear(self):
        self.color = Qt.white
        self.image.fill(Qt.white)
        self.update()

    def pixel_4(self):
        self.brushSize = 4

    def pixel_7(self):
        self.brushSize = 7

    def pixel_9(self):
        self.brushSize = 9

    def pixel_12(self):
        self.brushSize = 12

    def pixel_15(self):
        self.brushSize = 15

    def black_color(self):
        self.brushColor = Qt.black

    def green_color(self):
        self.brushColor = Qt.green

    def yellow_color(self):
        self.brushColor = Qt.yellow

    def red_color(self):
        self.brushColor = Qt.red

    def blue_color(self):
        self.brushColor = Qt.blue

    def white_color(self):
        self.brushColor = Qt.white

    def erase(self):
        self.brushColor = self.color

    def fill_blue(self):
        self.color = Qt.blue
        self.image.fill(Qt.blue)

    def fill_black(self):
        self.color = Qt.black
        self.image.fill(Qt.black)

    def fill_yellow(self):
        self.color = Qt.yellow
        self.image.fill(Qt.yellow)

    def fill_green(self):
        self.color = Qt.green
        self.image.fill(Qt.green)

    def fill_red(self):
        self.color = Qt.red
        self.image.fill(Qt.red)

    def fill_white(self):
        self.color = Qt.white
        self.image.fill(Qt.white)


App = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(App.exec())
