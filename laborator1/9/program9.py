import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class Fereastra(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Program 9")
        self.layout = QVBoxLayout(self)
        self.edit_a = QLineEdit()
        self.edit_b = QLineEdit()
        self.btn = QPushButton("Rezolva")
        self.label = QLabel("")
        self.edit_a.setPlaceholderText("a")
        self.edit_b.setPlaceholderText("b")
        self.layout.addWidget(self.edit_a)
        self.layout.addWidget(self.edit_b)
        self.layout.addWidget(self.btn)
        self.layout.addWidget(self.label)
        self.btn.clicked.connect(self.rezolva)

    def rezolva(self):
        try:
            a = float(self.edit_a.text())
            b = float(self.edit_b.text())
            if a > 0:
                sol = "x > " + str(-b/a)
            elif a < 0:
                sol = "x < " + str(-b/a)
            else:
                sol = "toate x" if b > 0 else "niciun x"
            self.label.setText(sol)
        except:
            self.label.setText("Date invalide")

app = QApplication(sys.argv)
f = Fereastra()
f.show()
sys.exit(app.exec_())