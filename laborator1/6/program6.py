import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

class Fereastra(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Program 6")
        self.layout = QVBoxLayout(self)
        self.label = QLabel("")
        self.layout.addWidget(self.label)
        self.setMouseTracking(True)

    def enterEvent(self, event):
        self.label.setText("Mouse pe forma")

    def leaveEvent(self, event):
        self.label.setText("Mouse in afara")

app = QApplication(sys.argv)
f = Fereastra()
f.show()
sys.exit(app.exec_())