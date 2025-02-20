import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QFont

class Fereastra(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Program 3")
        self.layout = QVBoxLayout(self)
        self.label = QLabel("Text")
        self.btn_mare = QPushButton("Mai mare")
        self.btn_mic = QPushButton("Mai mic")
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.btn_mare)
        self.layout.addWidget(self.btn_mic)
        self.font_size = 12
        font = QFont()
        font.setPointSize(self.font_size)
        self.label.setFont(font)
        self.btn_mare.clicked.connect(self.mareste)
        self.btn_mic.clicked.connect(self.micsoreaza)

    def mareste(self):
        self.font_size += 2
        font = self.label.font()
        font.setPointSize(self.font_size)
        self.label.setFont(font)

    def micsoreaza(self):
        self.font_size = max(2, self.font_size - 2)
        font = self.label.font()
        font.setPointSize(self.font_size)
        self.label.setFont(font)

app = QApplication(sys.argv)
f = Fereastra()
f.show()
sys.exit(app.exec_())