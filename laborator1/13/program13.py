import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton

class Fereastra(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Program 13")
        self.layout = QVBoxLayout(self)
        self.edit1 = QLineEdit()
        self.edit2 = QLineEdit()
        self.btn = QPushButton("Rasturneaza")
        self.layout.addWidget(self.edit1)
        self.layout.addWidget(self.edit2)
        self.layout.addWidget(self.btn)
        self.btn.clicked.connect(self.rasturneaza)
    def rasturneaza(self):
        self.edit2.setText(self.edit1.text()[::-1])

app = QApplication(sys.argv)
f = Fereastra()
f.show()
sys.exit(app.exec_())