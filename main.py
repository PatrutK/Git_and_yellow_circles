import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor

from random import randint


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.d = randint(25, 250)
        self.do_paint = False
        self.setGeometry(282, 200, 300, 300)
        self.setWindowTitle('Git и желтые окружности')

        self.push_btn = QPushButton(self)
        self.push_btn.resize(170, 60)
        self.push_btn.move(65, 100)
        self.push_btn.setText('Нарисовать круг')
        self.push_btn.clicked.connect(self.paint)

    def draw_elipse(self, qp):
        qp.setBrush(QColor('yellow'))
        qp.drawEllipse(10, 10, self.d, self.d)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_elipse(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()
        self.push_btn.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
