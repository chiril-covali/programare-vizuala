import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

class Fereastra(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Program 4")
        self.layout = QVBoxLayout(self)
        self.label = QLabel("0,0")
        self.layout.addWidget(self.label)
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        x = event.x()
        y = event.y()
        self.label.setText("{},{}".format(x, y))

app = QApplication(sys.argv)
f = Fereastra()
f.show()
sys.exit(app.exec_())