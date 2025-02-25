import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, 
                             QPushButton, QVBoxLayout, QRadioButton, QButtonGroup)
from PyQt5.QtGui import QDoubleValidator, QIntValidator

class DepositCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator Randament Depozit")
        self.init_ui()
        
    def init_ui(self):
        self.amount_label = QLabel("Suma Depozit (lei):")
        self.amount_edit = QLineEdit()
        self.amount_edit.setValidator(QDoubleValidator(0.0, 1000000.0, 2))
        
        self.years_label = QLabel("Număr de ani:")
        self.years_edit = QLineEdit()
        self.years_edit.setValidator(QIntValidator(1, 100))
        
        self.rate_label = QLabel("Rata dobânzii (% anual):")
        self.rate_edit = QLineEdit()
        self.rate_edit.setValidator(QDoubleValidator(0.0, 100.0, 2))
        
        self.simple_radio = QRadioButton("Dobândă Simplă")
        self.compound_radio = QRadioButton("Dobândă Compusă")
        self.simple_radio.setChecked(True)
        
        self.radio_group = QButtonGroup()
        self.radio_group.addButton(self.simple_radio)
        self.radio_group.addButton(self.compound_radio)
        
        self.calculate_btn = QPushButton("Calculează")
        self.calculate_btn.clicked.connect(self.calculate)
        
        self.result_label = QLabel("Randament:")
        
        layout = QVBoxLayout()
        layout.addWidget(self.amount_label)
        layout.addWidget(self.amount_edit)
        layout.addWidget(self.years_label)
        layout.addWidget(self.years_edit)
        layout.addWidget(self.rate_label)
        layout.addWidget(self.rate_edit)
        layout.addWidget(self.simple_radio)
        layout.addWidget(self.compound_radio)
        layout.addWidget(self.calculate_btn)
        layout.addWidget(self.result_label)
        self.setLayout(layout)
        
    def calculate(self):
        try:
            P = float(self.amount_edit.text())
            t = int(self.years_edit.text())
            r = float(self.rate_edit.text()) / 100.0
            if self.simple_radio.isChecked():
                # Dobânda simplă: A = P * (1 + r * t)
                A = P * (1 + r * t)
                interest_type = "Simplă"
            else:
                # Dobânda compusă (compunere lunară):
                n = 12
                A = P * (1 + r/n) ** (n * t)
                interest_type = "Compusă"
            self.result_label.setText(f"Randament ({interest_type}): {A:.2f} lei")
        except Exception:
            self.result_label.setText("Eroare: Verificați datele introduse.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DepositCalculator()
    window.show()
    sys.exit(app.exec_())