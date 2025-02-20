import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox

class Fereastra(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Program 14")
        self.layout = QVBoxLayout(self)
        self.edit = QLineEdit()
        self.btn1 = QPushButton("Afiseaza text")
        self.btn2 = QPushButton("Sterge text")
        self.btn3 = QPushButton("Iesire")
        self.layout.addWidget(self.edit)
        self.layout.addWidget(self.btn1)
        self.layout.addWidget(self.btn2)
        self.layout.addWidget(self.btn3)
        self.btn1.clicked.connect(self.afiseaza)
        self.btn2.clicked.connect(self.sterge)
        self.btn3.clicked.connect(self.close)
    def afiseaza(self):
        QMessageBox.information(self, "Mesaj", self.edit.text())
    def sterge(self):
        self.edit.clear()

app = QApplication(sys.argv)
f = Fereastra()
f.show()
sys.exit(app.exec_())