import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel

class Fereastra(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Program 16")
        self.layout = QVBoxLayout(self)
        self.editX = QLineEdit()
        self.editP = QLineEdit()
        self.editX1 = QLineEdit()
        self.editX.setPlaceholderText("X (kg)")
        self.editP.setPlaceholderText("P (lei/kg)")
        self.editX1.setPlaceholderText("X1 (kg alterate)")
        self.btn = QPushButton("Calculeaza")
        self.label = QLabel("")
        self.layout.addWidget(self.editX)
        self.layout.addWidget(self.editP)
        self.layout.addWidget(self.editX1)
        self.layout.addWidget(self.btn)
        self.layout.addWidget(self.label)
        self.btn.clicked.connect(self.calculeaza)
    def calculeaza(self):
        try:
            X = float(self.editX.text())
            P = float(self.editP.text())
            X1 = float(self.editX1.text())
            if X - X1 <= 0:
                self.label.setText("Date invalide")
                return
            pret_nou = (X * P)/(X - X1)
            diferenta = pret_nou - P
            self.label.setText(str(diferenta))
        except:
            self.label.setText("Eroare")

app = QApplication(sys.argv)
f = Fereastra()
f.show()
sys.exit(app.exec_())