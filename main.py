import sys

from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

from solve import getQuad


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.start_x, self.start_y = 300, 300
        self.width, self.height = 1200, 900
        self.scale = 1
        self.c_x, self.c_y = self.width // 2, self.height // 2
        self.my_dots = list()
        self.initUI()

    def initUI(self):
        self.setGeometry(self.start_x, self.start_y, self.width, self.height)
        self.setWindowTitle("Search max area")

        self.clear_btn = QPushButton("Очистить", self)
        self.clear_btn.resize(180, 100)
        self.clear_btn.move(round(self.width * 0.18), round(self.height * 0.01))
        self.clear_btn.clicked.connect(self.clear)

        self.add_btn = QPushButton("Добавить", self)
        self.add_btn.resize(180, 100)
        self.add_btn.move(round(self.width * 0.01), round(self.height * 0.01))


    def mousePressEvent(self, event):  # считывание точек с мышки
        x, y = event.x(), event.y()  # получаем координаты клика
        self.my_dots.append(((x - self.c_x + self.scale - 1) // self.scale, (self.c_y - y) // self.scale))
        self.update()

    def keyPressEvent(self, event):  # регистрируем нажатие на клавиатуру
        Main.focusInEvent()
        if int(event.modifiers()) == Qt.ControlModifier:
            if event.key() == Qt.Key_Left:  # стрелочка влево
                self.c_x += 10 * self.scale
            if event.key() == Qt.Key_Right:  # стрелочка вправо
                self.c_x -= 10 * self.scale
            if event.key() == Qt.Key_Down:  # стрелочка вниз
                self.c_y -= 10 * self.scale
            if event.key() == Qt.Key_Up:  # стрелочка вверх
                self.c_y += 10 * self.scale

    def clear(self):
        self.my_dots.clear()
        self.update()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.drawDots(painter)
        self.drawQaud(painter)
        painter.end()

    def drawDots(self, painter):  # рисует точки
        painter.setPen(QPen(Qt.gray, 5))  # выбираем цвет
        for x, y in self.my_dots:  # перебираем координаты всех точек
            painter.drawEllipse(self.c_x + x * self.scale, self.c_y - y * self.scale, 2, 2)

    def drawQaud(self, painter):
        painter.setPen(QPen(Qt.green, 3))  # выбираем цвет
        dots = list()
        for x, y in getQuad(self.my_dots):
            dots.append(QPointF(self.c_x + x * self.scale, self.c_y - y * self.scale))
        painter.drawPolygon(dots)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec())
