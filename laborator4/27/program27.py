#!/usr/bin/env python3
import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt

class HilbertWidget(QWidget):
    def __init__(self, order=5):
        super().__init__()
        self.order = order
        self.setWindowTitle("Curbă Hilbert")
        self.resize(600, 600)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        pen = QPen(Qt.black, 1)
        painter.setPen(pen)

        # Determinăm zona de desen cu un mic margine
        w = self.width()
        h = self.height()
        s = min(w, h)
        margin = s * 0.1
        drawing_size = s - 2 * margin

        # Pentru o curbă Hilbert de ordin n, numărul de celule este 2^n.
        # Considerăm că distanța dintre centrii celulelor este constantă.
        grid = 2**self.order - 1
        self.step = drawing_size / grid

        # Setăm sistemul de coordonate astfel încât originea să fie în stânga jos
        painter.translate(margin, drawing_size + margin)
        painter.scale(1, -1)  # Invertem axa Y pentru a desena cum se așteaptă

        self.painter = painter
        # Inițializăm "țestoasa" (turtle)
        self.x = 0
        self.y = 0
        self.heading = 0  # 0 grade: spre dreapta

        # Desenăm curbă Hilbert
        self.hilbert(self.order, 90)

    def hilbert(self, n, angle):
        if n == 0:
            return
        self.left(angle)
        self.hilbert(n - 1, -angle)
        self.forward(self.step)
        self.right(angle)
        self.hilbert(n - 1, angle)
        self.forward(self.step)
        self.hilbert(n - 1, angle)
        self.right(angle)
        self.forward(self.step)
        self.hilbert(n - 1, -angle)
        self.left(angle)

    def forward(self, step):
        rad = math.radians(self.heading)
        new_x = self.x + step * math.cos(rad)
        new_y = self.y + step * math.sin(rad)
        # Desenăm o linie de la poziția curentă la cea nouă
        self.painter.drawLine(round(self.x), round(self.y), round(new_x), round(new_y))
        self.x = new_x
        self.y = new_y

    def left(self, angle):
        self.heading += angle

    def right(self, angle):
        self.heading -= angle

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HilbertWidget(order=5)
    window.show()
    sys.exit(app.exec_())