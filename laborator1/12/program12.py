import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel

def este_prim(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def suma_cifrelor(n):
    s = 0
    for c in str(abs(n)):
        if c.isdigit():
            s += int(c)
    return s

def ultimacifra(n):
    return abs(n) % 10

def cel_mai_mare_divizor_prim(n):
    n = abs(n)
    divizor = -1
    for i in range(2, n):
        if n % i == 0 and este_prim(i):
            divizor = i
    return divizor

class Fereastra(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Program 12")
        self.layout = QVBoxLayout(self)
        self.edit = QLineEdit()
        self.btn = QPushButton("Calculeaza")
        self.label = QLabel("")
        self.layout.addWidget(self.edit)
        self.layout.addWidget(self.btn)
        self.layout.addWidget(self.label)
        self.btn.clicked.connect(self.calculeaza)
    def calculeaza(self):
        try:
            nr = int(self.edit.text())
            uc = ultimacifra(nr)
            s = suma_cifrelor(nr)
            prim = "este prim" if este_prim(nr) else "nu este prim"
            d = cel_mai_mare_divizor_prim(nr)
            d_str = str(d) if d != -1 else "nu exista"
            rezultat = "Ultima cifra: " + str(uc) + " | Suma cifrelor: " + str(s) + " | " + prim + " | Divizor prim: " + d_str
            self.label.setText(rezultat)
        except:
            self.label.setText("Eroare")

app = QApplication(sys.argv)
f = Fereastra()
f.show()
sys.exit(app.exec_())