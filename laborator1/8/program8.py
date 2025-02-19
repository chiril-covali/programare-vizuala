import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit
from PyQt5.QtGui import QColor, QPalette

class Fereastra(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Semafor")
        self.layout = QVBoxLayout(self)
        self.edit = QLineEdit()
        self.layout.addWidget(self.edit)
        self.btn_layout = QHBoxLayout()
        self.btn_rosu = QPushButton("Rosu")
        self.btn_galben = QPushButton("Galben")
        self.btn_verde = QPushButton("Verde")
        self.btn_layout.addWidget(self.btn_rosu)
        self.btn_layout.addWidget(self.btn_galben)
        self.btn_layout.addWidget(self.btn_verde)
        self.layout.addLayout(self.btn_layout)
        self.btn_rosu.clicked.connect(lambda: self.schimba_culoare("rosu"))
        self.btn_galben.clicked.connect(lambda: self.schimba_culoare("galben"))
        self.btn_verde.clicked.connect(lambda: self.schimba_culoare("verde"))

    def schimba_culoare(self, culoare):
        self.edit.setText(culoare)
        palette = self.edit.palette()
        if culoare == "rosu":
            palette.setColor(QPalette.Text, QColor("red"))
        elif culoare == "galben":
            palette.setColor(QPalette.Text, QColor("yellow"))
        elif culoare == "verde":
            palette.setColor(QPalette.Text, QColor("green"))
        self.edit.setPalette(palette)

app = QApplication(sys.argv)
f = Fereastra()
f.show()
sys.exit(app.exec_())