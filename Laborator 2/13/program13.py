import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
                             QPushButton, QVBoxLayout, QRadioButton, QButtonGroup)
from PyQt5.QtGui import QDoubleValidator

class CircuitCurrentCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calcul Curent Circuit")
        self.init_ui()
        
    def init_ui(self):
        self.res1_label = QLabel("Rezistența R1 (ohmi):")
        self.res1_edit = QLineEdit()
        self.res1_edit.setValidator(QDoubleValidator(0.0, 1e6, 2))
        
        self.res2_label = QLabel("Rezistența R2 (ohmi):")
        self.res2_edit = QLineEdit()
        self.res2_edit.setValidator(QDoubleValidator(0.0, 1e6, 2))
        
        self.series_radio = QRadioButton("Serie")
        self.parallel_radio = QRadioButton("Paralel")
        self.series_radio.setChecked(True)
        
        self.radio_group = QButtonGroup()
        self.radio_group.addButton(self.series_radio)
        self.radio_group.addButton(self.parallel_radio)
        
        self.calculate_btn = QPushButton("Calculează")
        self.calculate_btn.clicked.connect(self.calculate)
        
        self.result_label = QLabel("Curentul circuitului (A):")
        
        layout = QVBoxLayout()
        layout.addWidget(self.res1_label)
        layout.addWidget(self.res1_edit)
        layout.addWidget(self.res2_label)
        layout.addWidget(self.res2_edit)
        layout.addWidget(self.series_radio)
        layout.addWidget(self.parallel_radio)
        layout.addWidget(self.calculate_btn)
        layout.addWidget(self.result_label)
        self.setLayout(layout)
        
    def calculate(self):
        try:
            R1 = float(self.res1_edit.text())
            R2 = float(self.res2_edit.text())
            if self.series_radio.isChecked():
                R_total = R1 + R2
            else:
                if R1 == 0 or R2 == 0:
                    self.result_label.setText("Rezistența nu poate fi 0 pentru conexiune paralelă.")
                    return
                R_total = 1 / (1 / R1 + 1 / R2)
            I = 220 / R_total if R_total != 0 else 0
            self.result_label.setText(f"Curentul circuitului: {I:.2f} A")
        except Exception:
            self.result_label.setText("Eroare: Verificați inputul.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CircuitCurrentCalculator()
    window.show()
    sys.exit(app.exec_())