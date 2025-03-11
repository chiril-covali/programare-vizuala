import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt

class OlympicFlag(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(100, 100, 800, 400)
        self.setWindowTitle('Drapel Olimpic')
        self.show()
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Configurarea stilului pentru cercuri
        pen = QPen(Qt.black, 3)
        painter.setPen(pen)
        
        # Dimensiunile și pozițiile cercurilor
        diameter = 100
        y = self.height() // 2
        spacing = diameter + 10
        
        # Desenarea cercurilor olimpice
        # Primul rând
        painter.setPen(QPen(Qt.blue, 3))
        painter.drawEllipse(200, y - diameter//2, diameter, diameter)  # Albastru
        
        painter.setPen(QPen(Qt.black, 3))
        painter.drawEllipse(200 + spacing, y - diameter//2, diameter, diameter)  # Negru
        
        painter.setPen(QPen(Qt.red, 3))
        painter.drawEllipse(200 + spacing * 2, y - diameter//2, diameter, diameter)  # Roșu
        
        # Al doilea rând (ușor deplasat în jos și la dreapta)
        painter.setPen(QPen(Qt.darkYellow, 3))
        painter.drawEllipse(int(200 + spacing//2), y + 10, diameter, diameter)  # Galben
        
        painter.setPen(QPen(Qt.darkGreen, 3))
        painter.drawEllipse(int(200 + spacing * 1.5), y + 10, diameter, diameter)  # Verde

def main():
    app = QApplication(sys.argv)
    ex = OlympicFlag()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()