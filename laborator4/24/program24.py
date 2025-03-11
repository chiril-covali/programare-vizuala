import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QPen, QPixmap
from PyQt5.QtCore import Qt

class MoldovaFlag(QMainWindow):
    def __init__(self):
        super().__init__()
        self.stema = QPixmap('/Users/covali/Desktop/programare-vizuala-main/laborator4/24/stema.png')
        self.initUI()
        
    def initUI(self):
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle('Drapelul Republicii Moldova')
        self.show()
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Dimensiunile drapelului
        width = self.width()
        height = self.height()
        stripe_width = width // 3
        
        # Desenarea dungilor verticale cu culorile specificate
        # Albastru
        painter.fillRect(0, 0, stripe_width, height, QColor('#0046AE'))
        # Galben
        painter.fillRect(stripe_width, 0, stripe_width, height, QColor('#FFD200'))
        # Roșu
        painter.fillRect(stripe_width * 2, 0, stripe_width, height, QColor('#CC092F'))
        
        # Calcularea dimensiunii și poziției stemei
        stema_width = stripe_width * 0.6
        stema_height = height * 0.6
        stema_x = (width - stema_width) // 2
        stema_y = (height - stema_height) // 2
        
        # Desenarea stemei în centru
        scaled_stema = self.stema.scaled(int(stema_width), int(stema_height), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        painter.drawPixmap(int(stema_x), int(stema_y), scaled_stema)

def main():
    app = QApplication(sys.argv)
    ex = MoldovaFlag()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()