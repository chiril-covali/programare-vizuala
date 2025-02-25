import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QDoubleValidator

class DiscountCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calcul Preț cu Reducere")
        self.init_ui()

    def init_ui(self):
        self.input_label = QLabel("Introduceți suma de cumpărare (ruble):")
        self.input_edit = QLineEdit()
        self.input_edit.setValidator(QDoubleValidator(0.0, 1e6, 2, self))
        self.calculate_btn = QPushButton("Calculează")
        self.calculate_btn.clicked.connect(self.calculate)
        
        layout = QVBoxLayout()
        layout.addWidget(self.input_label)
        layout.addWidget(self.input_edit)
        layout.addWidget(self.calculate_btn)
        self.setLayout(layout)
    
    def calculate(self):
        try:
            amount = float(self.input_edit.text())
            discount_pct = 0
            if amount > 1000:
                discount_pct = 3
            elif amount > 500:
                discount_pct = 2
            elif amount > 300:
                discount_pct = 1
            
            discount_value = amount * discount_pct / 100
            final_price = amount - discount_value
            
            msg = QMessageBox()
            msg.setWindowTitle("Reducere")
            msg.setText(f"Reducere: {discount_pct}%\nValoare reducere: {discount_value:.2f} ruble\nPreț final: {final_price:.2f} ruble")
            msg.exec_()
        except ValueError:
            pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DiscountCalculator()
    window.show()
    sys.exit(app.exec_())