import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel

class Fereastra(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Program 20")
        self.layout = QVBoxLayout(self)
        self.edit1 = QLineEdit()
        self.edit2 = QLineEdit()
        self.edit1.setPlaceholderText("Ziua saptamanii a 1 ian (1-7)")
        self.edit2.setPlaceholderText("Ziua anului (1-366)")
        self.btn = QPushButton("Calculeaza saptamana")
        self.label = QLabel("")
        self.layout.addWidget(self.edit1)
        self.layout.addWidget(self.edit2)
        self.layout.addWidget(self.btn)
        self.layout.addWidget(self.label)
        self.btn.clicked.connect(self.calculeaza)
    def calculeaza(self):
        try:
            f = int(self.edit1.text())
            n = int(self.edit2.text())
            saptamana = ((n + (f - 1) - 1) // 7) + 1
            self.label.setText(str(saptamana))
        except:
            self.label.setText("Eroare")

app = QApplication(sys.argv)
f = Fereastra()
f.show()
sys.exit(app.exec_())