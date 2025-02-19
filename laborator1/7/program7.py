import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt, QPoint
from math import hypot

class Fereastra(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Program 7")
        self.resize(300,200)
        self.label1 = QLabel("Eticheta 1", self)
        self.label2 = QLabel("Eticheta 2", self)
        self.label1.setGeometry(50,50,100,30)
        self.label2.setGeometry(150,120,100,30)
        self.label1.setStyleSheet("background-color: white;")
        self.label2.setStyleSheet("background-color: white;")
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        p = event.pos()
        c1 = self.label1.geometry().center()
        c2 = self.label2.geometry().center()
        d1 = hypot(p.x()-c1.x(), p.y()-c1.y())
        d2 = hypot(p.x()-c2.x(), p.y()-c2.y())
        if d1 < d2:
            self.label1.setStyleSheet("background-color: red;")
            self.label2.setStyleSheet("background-color: white;")
        else:
            self.label1.setStyleSheet("background-color: white;")
            self.label2.setStyleSheet("background-color: red;")

app = QApplication(sys.argv)
f = Fereastra()
f.show()
sys.exit(app.exec_())