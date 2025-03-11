import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QTimer


class ShipWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Animație cu navă')
        self.setGeometry(100, 100, 800, 400)
        
        # Poziția navei și mișcarea
        self.ship_x = 0
        self.ship_y = 200
        self.direction = 1  # 1 pentru dreapta, -1 pentru stânga
        
        # Timer pentru animație
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.move_ship)
        self.timer.start(50)  # Actualizare la fiecare 50ms
        
    def move_ship(self):
        # Actualizează poziția navei
        self.ship_x += 5 * self.direction
        
        # Inversează direcția când se atinge marginea ferestrei
        if self.ship_x > self.width():
            self.direction = -1
        elif self.ship_x < 0:
            self.direction = 1
            
        self.update()  # Declanșează repaint

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Desenează apă
        painter.fillRect(0, self.height() // 2, self.width(), self.height() // 2, QColor(0, 100, 190))
        
        # Desenează nava
        self.draw_ship(painter)
        
    def draw_ship(self, painter):
        # Desenează corpul navei
        painter.setPen(QPen(Qt.black, 2))
        painter.setBrush(QColor(139, 69, 19))  # Culoare maro
        
        hull_points = [
            (self.ship_x, self.ship_y),
            (self.ship_x + 100, self.ship_y),
            (self.ship_x + 80, self.ship_y + 40),
            (self.ship_x + 20, self.ship_y + 40)
        ]
        
        # Desenează conturul corpului
        for i in range(len(hull_points)):
            if i < len(hull_points) - 1:
                painter.drawLine(hull_points[i][0], hull_points[i][1],
                                 hull_points[i + 1][0], hull_points[i + 1][1])
            else:
                painter.drawLine(hull_points[i][0], hull_points[i][1],
                                 hull_points[0][0], hull_points[0][1])
        
        # Desenează catargul
        painter.drawLine(self.ship_x + 50, self.ship_y,
                         self.ship_x + 50, self.ship_y - 60)
        
        # Desenează pânza
        sail_points = [
            (self.ship_x + 50, self.ship_y - 60),
            (self.ship_x + 80, self.ship_y - 30),
            (self.ship_x + 50, self.ship_y)
        ]
        
        painter.setBrush(QColor(255, 255, 255))  # Culoare albă pentru pânză
        for i in range(len(sail_points)):
            if i < len(sail_points) - 1:
                painter.drawLine(sail_points[i][0], sail_points[i][1],
                                 sail_points[i + 1][0], sail_points[i + 1][1])
            else:
                painter.drawLine(sail_points[i][0], sail_points[i][1],
                                 sail_points[0][0], sail_points[0][1])

def main():
    app = QApplication(sys.argv)
    window = ShipWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()