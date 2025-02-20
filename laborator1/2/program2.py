import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QInputDialog

class Fereastra(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Program 2")
        self.layout = QVBoxLayout(self)
        self.btn = QPushButton("Introdu cuvant")
        self.label = QLabel("")
        self.layout.addWidget(self.btn)
        self.layout.addWidget(self.label)
        self.btn.clicked.connect(self.cere_cuvant)

    def cere_cuvant(self):
        cuvant, ok = QInputDialog.getText(self, "Cuvant", "Introdu cuvantul:")
        if ok and cuvant:
            vocale = "aeiouAEIOU"
            nr_vocale = sum(1 for c in cuvant if c in vocale)
            nr_consoane = sum(1 for c in cuvant if c.isalpha() and c not in vocale)
            self.label.setText("Vocale: {} | Consoane: {}".format(nr_vocale, nr_consoane))

app = QApplication(sys.argv)
f = Fereastra()
f.show()
sys.exit(app.exec_())