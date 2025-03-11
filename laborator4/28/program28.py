#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPen, QFont
from PyQt5.QtCore import Qt

class GridForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grilă de coordonate digitalizate")
        self.resize(600, 600)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        width = self.width()
        height = self.height()

        # Stabilim spațiul dintre liniile grilei
        spacing = 20

        # Desenăm liniile grilei (linii verticale și orizontale)
        gridPen = QPen(Qt.lightGray, 1, Qt.SolidLine)
        painter.setPen(gridPen)
        
        # Linie verticală
        x = 0
        while x <= width:
            painter.drawLine(x, 0, x, height)
            x += spacing

        # Linie orizontală
        y = 0
        while y <= height:
            painter.drawLine(0, y, width, y)
            y += spacing

        # Desenăm axele de coordonate cu o culoare și grosime mai accentuate
        axisPen = QPen(Qt.black, 2)
        painter.setPen(axisPen)
        
        # Linia axei X - centrul ferestrei pe verticală
        centerY = height // 2
        painter.drawLine(0, centerY, width, centerY)
        
        # Linia axei Y - centrul ferestrei pe orizontală
        centerX = width // 2
        painter.drawLine(centerX, 0, centerX, height)
        
        # Opțional: Adăugăm etichete pentru axe
        painter.setPen(Qt.darkBlue)
        font = QFont("Arial", 10)
        painter.setFont(font)
        
        # Etichete pentru axa X
        num_labels = width // spacing
        for i in range(-num_labels//2, num_labels//2 + 1):
            xPos = centerX + i * spacing
            if i != 0:
                painter.drawText(xPos - 10, centerY - 5, f"{i*spacing}")
        
        # Etichete pentru axa Y
        num_labels = height // spacing
        for j in range(-num_labels//2, num_labels//2 + 1):
            yPos = centerY + j * spacing
            if j != 0:
                painter.drawText(centerX + 5, yPos + 5, f"{-j*spacing}")
        
        painter.end()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GridForm()
    window.show()
    sys.exit(app.exec_())