import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel

class Fereastra(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Program 18")
        self.layout = QVBoxLayout(self)
        self.edit = QLineEdit()
        self.btn = QPushButton("Evalueaza")
        self.label = QLabel("")
        self.layout.addWidget(self.edit)
        self.layout.addWidget(self.btn)
        self.layout.addWidget(self.label)
        self.btn.clicked.connect(self.evalueaza)
    def evalueaza(self):
        try:
            rezultat = eval(self.edit.text())
            self.label.setText(str(rezultat))
        except:
            self.label.setText("Eroare")

app = QApplication(sys.argv)
f = Fereastra()
f.show()
sys.exit(app.exec_())