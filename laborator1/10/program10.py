import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton

class Fereastra(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Program 10")
        self.layout = QVBoxLayout(self)
        self.edit = QLineEdit()
        self.btn = QPushButton("Mare litere")
        self.layout.addWidget(self.edit)
        self.layout.addWidget(self.btn)
        self.btn.clicked.connect(self.mare_litere)

    def mare_litere(self):
        self.edit.setText(self.edit.text().upper())

app = QApplication(sys.argv)
f = Fereastra()
f.show()
sys.exit(app.exec_())