import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QIntValidator

class PurchaseCostCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Costul de Achiziție")
        # Dicționarul de produse: cod produs => {"nume": numeProdus, "pret": pretProdus}
        self.products = {
            "101": {"name": "Măr", "price": 2.50},
            "102": {"name": "Păr", "price": 3.00},
            "103": {"name": "Banane", "price": 1.80},
            "104": {"name": "Portocale", "price": 2.20},
        }
        self.init_ui()

    def init_ui(self):
        self.code_label = QLabel("Introduceți codul produsului:")
        self.code_edit = QLineEdit()
        self.quantity_label = QLabel("Introduceți numărul de unități:")
        self.quantity_edit = QLineEdit()
        self.quantity_edit.setValidator(QIntValidator(1, 10000, self))
        self.calculate_btn = QPushButton("Calculează costul")
        self.calculate_btn.clicked.connect(self.calculate)
        self.result_label = QLabel("Costul total:")

        layout = QVBoxLayout()
        layout.addWidget(self.code_label)
        layout.addWidget(self.code_edit)
        layout.addWidget(self.quantity_label)
        layout.addWidget(self.quantity_edit)
        layout.addWidget(self.calculate_btn)
        layout.addWidget(self.result_label)
        self.setLayout(layout)
    
    def calculate(self):
        code = self.code_edit.text().strip()
        if code not in self.products:
            QMessageBox.warning(self, "Eroare", "Produsul cu codul introdus nu există!")
            return
        try:
            quantity = int(self.quantity_edit.text())
        except ValueError:
            self.result_label.setText("Introduceți o cantitate validă.")
            return
        product = self.products[code]
        total = product["price"] * quantity
        self.result_label.setText(f"{product['name']} x {quantity} = {total:.2f} ruble")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PurchaseCostCalculator()
    window.show()
    sys.exit(app.exec_())