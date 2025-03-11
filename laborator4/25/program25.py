import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtCore import Qt, QPoint
import math

class StarWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.stars = []
        
    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Stea cu cinci vârfuri')
        self.show()
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.stars.append(event.pos())
            self.update()
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Configurare stil pentru stea
        pen = QPen(Qt.yellow, 2)
        painter.setPen(pen)
        # Setare culoare de umplere galbenă
        painter.setBrush(QBrush(Qt.yellow))
        
        # Desenare stele pentru fiecare click
        for pos in self.stars:
            self.drawStar(painter, pos.x(), pos.y())
    
    def drawStar(self, painter, cx, cy):
        # Parametri stea
        outer_radius = 50  # Raza exterioară
        inner_radius = 20  # Raza interioară
        points = []
        
        # Calculare puncte pentru stea
        for i in range(10):
            angle = math.pi / 2 + (2 * math.pi * i) / 10
            radius = outer_radius if i % 2 == 0 else inner_radius
            
            x = cx + radius * math.cos(angle)
            y = cy + radius * math.sin(angle)
            points.append(QPoint(int(x), int(y)))
        
        # Desenare stea umplută
        painter.drawPolygon(*points)

def main():
    app = QApplication(sys.argv)
    ex = StarWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()