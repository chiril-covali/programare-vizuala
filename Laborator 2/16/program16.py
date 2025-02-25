import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QGridLayout, QVBoxLayout, QMessageBox

class SimpleCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator Adunare și Scădere")
        self.initUI()
        
    def initUI(self):
        # Display pentru introducerea expresiei și afișarea rezultatului
        self.display = QLineEdit(self)
        self.display.setReadOnly(True)
        
        # Creare butoane numerice 0-9 și conectarea unui handler comun
        self.buttons = {}
        for digit in range(10):
            self.buttons[str(digit)] = QPushButton(str(digit), self)
            self.buttons[str(digit)].clicked.connect(self.on_number_click)
            
        # Creare butoane pentru operatori și alte acțiuni
        self.add_button = QPushButton("+", self)
        self.sub_button = QPushButton("-", self)
        self.eq_button = QPushButton("=", self)
        self.clear_button = QPushButton("Clear", self)
        
        self.add_button.clicked.connect(self.on_operator_click)
        self.sub_button.clicked.connect(self.on_operator_click)
        self.eq_button.clicked.connect(self.on_equals)
        self.clear_button.clicked.connect(self.on_clear)
        
        # Layout pentru butoanele numerice (dispunere în grilă)
        grid = QGridLayout()
        # Dispunerea butoanelor: 7,8,9; 4,5,6; 1,2,3; 0
        positions = [(i, j) for i in range(4) for j in range(3)]
        num_order = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0']
        pos_map = {}
        index = 0
        for position in positions:
            if index < len(num_order):
                pos_map[num_order[index]] = position
                index += 1
                
        for num, pos in pos_map.items():
            grid.addWidget(self.buttons[num], pos[0], pos[1])
        
        # Layout vertical pentru operatori
        operator_layout = QVBoxLayout()
        operator_layout.addWidget(self.add_button)
        operator_layout.addWidget(self.sub_button)
        operator_layout.addWidget(self.eq_button)
        operator_layout.addWidget(self.clear_button)
        
        # Layout principal
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.display)
        main_layout.addLayout(grid)
        main_layout.addLayout(operator_layout)
        
        self.setLayout(main_layout)
        
    def on_number_click(self):
        sender = self.sender()  # Butonul care a fost apăsat
        num = sender.text()
        current_text = self.display.text()
        self.display.setText(current_text + num)
        
    def on_operator_click(self):
        sender = self.sender()
        op = sender.text()
        current_text = self.display.text()
        # Evităm operatorii consecutivi
        if current_text and current_text[-1] not in "+-":
            self.display.setText(current_text + op)
        elif current_text:
            # Înlocuim ultimul operator dacă se apasă un nou operator
            self.display.setText(current_text[:-1] + op)
            
    def on_equals(self):
        expression = self.display.text()
        try:
            # Evaluăm expresia care conține numai cifre și operatori +, -
            result = eval(expression)
            self.display.setText(str(result))
        except Exception:
            QMessageBox.warning(self, "Eroare", "Expresie invalidă.")
            
    def on_clear(self):
        self.display.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = SimpleCalculator()
    calculator.show()
    sys.exit(app.exec_())