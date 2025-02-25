import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QDoubleValidator

class ParallelCurrentCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calcul Curent în Circuit Paralel")
        self.init_ui()

    def init_ui(self):
        self.res1_label = QLabel("Rezistența R1 (ohmi):")
        self.res1_edit = QLineEdit()
        self.res1_edit.setValidator(QDoubleValidator(0.0, 1e6, 2, self))
        
        self.res2_label = QLabel("Rezistența R2 (ohmi):")
        self.res2_edit = QLineEdit()
        self.res2_edit.setValidator(QDoubleValidator(0.0, 1e6, 2, self))
        
        self.calculate_btn = QPushButton("Calculare")
        self.calculate_btn.clicked.connect(self.calculate)
        self.result_label = QLabel("Curentul (A):")
        
        layout = QGridLayout()
        layout.addWidget(self.res1_label, 0, 0)
        layout.addWidget(self.res1_edit, 0, 1)
        layout.addWidget(self.res2_label, 1, 0)
        layout.addWidget(self.res2_edit, 1, 1)
        layout.addWidget(self.calculate_btn, 2, 0, 1, 2)
        layout.addWidget(self.result_label, 3, 0, 1, 2)
        self.setLayout(layout)
    
    def calculate(self):
        try:
            R1 = float(self.res1_edit.text())
            R2 = float(self.res2_edit.text())
            if R1<=0 or R2<=0:
                self.result_label.setText("Rezistențele trebuie să fie > 0.")
                return
            # Rezistență echivalentă pentru două rezistențe în paralel:
            R_eq = 1 / (1/R1 + 1/R2)
            I = 220 / R_eq
            self.result_label.setText(f"Curentul (A): {I:.2f}")
        except ValueError:
            self.result_label.setText("Introduceți valori numerice valide.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ParallelCurrentCalculator()
    window.show()
    sys.exit(app.exec_())