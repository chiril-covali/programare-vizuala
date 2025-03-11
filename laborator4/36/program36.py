import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtCore import Qt, QTimer

class PlaneWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Animație cu avion')
        self.setGeometry(100, 100, 800, 600)

        # Determină directorul curent și formează calea completă spre imagini
        current_dir = os.path.dirname(os.path.abspath(__file__))
        background_path = os.path.join(current_dir, 'background.png')
        plane_path = os.path.join(current_dir, 'plane.png')

        # Încărcarea imaginilor din fișiere (asigurați-vă că fișierele există în acest director)
        self.background = QPixmap(background_path)
        self.plane = QPixmap(plane_path)

        # Scalăm avionul pentru a fi mult mai mic
        self.plane = self.plane.scaled(
            self.plane.width() // 2,
            self.plane.height() // 2,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        
        # Poziția inițială a obiectului în mișcare (avionul poziționat în partea de sus)
        self.plane_x = -self.plane.width()
        self.plane_y = 20  # poziționează avionul sus
        
        # Timer pentru animație
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.move_plane)
        self.timer.start(50)
        
    def move_plane(self):
        # Mișcă avionul pe orizontală
        self.plane_x += 5
        if self.plane_x > self.width():
            self.plane_x = -self.plane.width()
        self.update()
        
    def paintEvent(self, event):
        painter = QPainter(self)
        
        # Desenează imaginea de fundal scalată la dimensiunea ferestrei
        scaled_background = self.background.scaled(
            self.size(),
            Qt.KeepAspectRatioByExpanding,
            Qt.SmoothTransformation
        )
        painter.drawPixmap(0, 0, scaled_background)
        
        # Desenează imaginea avionului în mișcare (acum mai mic și poziționat sus)
        painter.drawPixmap(self.plane_x, self.plane_y, self.plane)

def main():
    app = QApplication(sys.argv)
    window = PlaneWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()