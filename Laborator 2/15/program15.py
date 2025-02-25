import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class TripCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Calculator Cost Călătorie")
        
        # Etichete și câmpuri de input
        self.distance_label = QLabel("Distanța (km):", self)
        self.distance_input = QLineEdit(self)
        
        self.fuel_label = QLabel("Consum (l/100km):", self)
        self.fuel_input = QLineEdit(self)
        
        self.price_label = QLabel("Preț combustibil (MDL/l):", self)
        self.price_input = QLineEdit(self)
        
        self.result_label = QLabel("Cost total:", self)
        
        self.calc_button = QPushButton("Calculează", self)
        self.calc_button.clicked.connect(self.calculate_cost)
        
        # Layout vertical
        layout = QVBoxLayout()
        layout.addWidget(self.distance_label)
        layout.addWidget(self.distance_input)
        layout.addWidget(self.fuel_label)
        layout.addWidget(self.fuel_input)
        layout.addWidget(self.price_label)
        layout.addWidget(self.price_input)
        layout.addWidget(self.calc_button)
        layout.addWidget(self.result_label)
        
        self.setLayout(layout)
        
    def calculate_cost(self):
        try:
            distance = float(self.distance_input.text())
            consumption = float(self.fuel_input.text())
            price = float(self.price_input.text())
            
            cost = distance * (consumption / 100) * price
            self.result_label.setText(f"Cost total: {cost:.2f} MDL")
        except ValueError:
            QMessageBox.warning(self, "Eroare", "Introduceți valori numerice valide.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = TripCalculator()
    calculator.show()
    sys.exit(app.exec_())