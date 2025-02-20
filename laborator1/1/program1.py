import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit

class Fereastra(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Program 1")
        self.layout = QVBoxLayout(self)
        self.label = QLabel("")
        self.btn_input = QPushButton("Afiseaza Input")
        self.btn_sterge = QPushButton("Sterge Label")
        self.edit = QLineEdit()
        self.edit.hide()
        self.layout.addWidget(self.btn_input)
        self.layout.addWidget(self.btn_sterge)
        self.layout.addWidget(self.edit)
        self.layout.addWidget(self.label)
        self.btn_input.clicked.connect(self.afiseaza_edit)
        self.edit.returnPressed.connect(self.actualizeaza_label)
        self.btn_sterge.clicked.connect(self.sterge_label)

    def afiseaza_edit(self):
        self.edit.show()
        self.edit.setFocus()

    def actualizeaza_label(self):
        self.label.setText(self.edit.text())

    def sterge_label(self):
        self.label.setText("")

app = QApplication(sys.argv)
f = Fereastra()
f.show()
sys.exit(app.exec_())