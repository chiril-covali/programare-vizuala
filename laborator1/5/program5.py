import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

class Fereastra(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Program 5")
        self.layout = QVBoxLayout(self)
        self.label_dim = QLabel("")
        self.label_mouse = QLabel("")
        self.layout.addWidget(self.label_dim)
        self.layout.addWidget(self.label_mouse)
        self.setMouseTracking(True)

    def resizeEvent(self, event):
        w = self.width()
        h = self.height()
        self.label_dim.setText("Dimensiuni: {}x{}".format(w, h))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.label_mouse.setText("Mouse: apasat")

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.label_mouse.setText("Mouse: ridicat")

app = QApplication(sys.argv)
f = Fereastra()
f.show()
sys.exit(app.exec_())