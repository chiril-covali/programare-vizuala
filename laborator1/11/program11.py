import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel

class Fereastra(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Program 11")
        self.layout = QVBoxLayout(self)
        self.edit = QLineEdit()
        self.btn = QPushButton("Calculeaza patrat")
        self.label = QLabel("")
        self.layout.addWidget(self.edit)
        self.layout.addWidget(self.btn)
        self.layout.addWidget(self.label)
        self.btn.clicked.connect(self.calculeaza)
    def calculeaza(self):
        try:
            nr = float(self.edit.text())
            self.label.setText(str(nr*nr))
        except:
            self.label.setText("Eroare")

app = QApplication(sys.argv)
f = Fereastra()
f.show()
sys.exit(app.exec_())