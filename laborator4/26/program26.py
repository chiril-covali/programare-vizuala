import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush
from PyQt5.QtCore import Qt, QRect, QPoint
import random

class SmileyGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.clicks = 0
        self.smiley_pos = QPoint(200, 200)
        self.smiley_size = 100
        self.initUI()
        
    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Prinde 10 fețe zâmbitoare')
        
        # Etichetă pentru scor
        self.score_label = QLabel(self)
        self.score_label.setGeometry(10, 10, 200, 30)
        self.updateScore()
        
        self.show()
    
    def updateScore(self):
        self.score_label.setText(f'Fețe prinse: {self.clicks}/10')
    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # Verifică dacă click-ul este pe față
            smiley_rect = QRect(
                self.smiley_pos.x() - self.smiley_size//2,
                self.smiley_pos.y() - self.smiley_size//2,
                self.smiley_size,
                self.smiley_size
            )
            
            if smiley_rect.contains(event.pos()):
                self.clicks += 1
                self.updateScore()
                
                if self.clicks >= 10:
                    self.close()
                else:
                    # Mută fața în poziție aleatoare
                    margin = self.smiley_size // 2
                    self.smiley_pos = QPoint(
                        random.randint(margin, self.width() - margin),
                        random.randint(margin, self.height() - margin)
                    )
                    self.update()
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Desenează fața zâmbitoare
        center = self.smiley_pos
        size = self.smiley_size
        
        # Cercul feței
        painter.setPen(QPen(Qt.black, 2))
        painter.setBrush(QBrush(QColor(255, 255, 0)))
        painter.drawEllipse(center, size//2, size//2)
        
        # Ochii
        eye_radius = size//10
        painter.setBrush(QBrush(Qt.black))
        painter.drawEllipse(center + QPoint(-size//4, -size//4), eye_radius, eye_radius)
        painter.drawEllipse(center + QPoint(size//4, -size//4), eye_radius, eye_radius)
        
        # Zâmbet
        painter.setPen(QPen(Qt.black, 3))
        painter.drawArc(
            QRect(center.x() - size//3, center.y() - size//3, 2*size//3, 2*size//3),
            0, -180 * 16
        )

def main():
    app = QApplication(sys.argv)
    ex = SmileyGame()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()