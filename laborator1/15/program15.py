import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton

class Fereastra(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Program 15")
        self.layout = QVBoxLayout(self)
        self.edit = QLineEdit()
        self.btn1 = QPushButton("Buton 1")
        self.btn2 = QPushButton("Buton 2")
        self.btn3 = QPushButton("Sterge")
        self.layout.addWidget(self.edit)
        self.layout.addWidget(self.btn1)
        self.layout.addWidget(self.btn2)
        self.layout.addWidget(self.btn3)
        self.btn1.clicked.connect(self.click1)
        self.btn2.clicked.connect(self.click2)
        self.btn3.clicked.connect(self.edit.clear)
    def click1(self):
        self.edit.setText("A fost executat un click pe butonul 1")
    def click2(self):
        self.edit.setText("A executat un click pe butonul 2")

app = QApplication(sys.argv)
f = Fereastra()
f.show()
sys.exit(app.exec_())