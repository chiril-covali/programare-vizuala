import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtGui import QDoubleValidator

class PoundToKgPositive(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Livre în Kilograme - Număr pozitiv")
        self.init_ui()

    def init_ui(self):
        self.input_label = QLabel("Introduceți masa (lire):")
        self.input_edit = QLineEdit()
        validator = QDoubleValidator(0.0, 10000.0, 3, self)
        self.input_edit.setValidator(validator)
        self.result_label = QLabel("Masa în kilograme:")
        self.calculate_btn = QPushButton("Calculează")
        self.calculate_btn.clicked.connect(self.calculate)
        
        layout = QVBoxLayout()
        layout.addWidget(self.input_label)
        layout.addWidget(self.input_edit)
        layout.addWidget(self.calculate_btn)
        layout.addWidget(self.result_label)
        self.setLayout(layout)
    
    def calculate(self):
        try:
            lb = float(self.input_edit.text())
            kg = lb * 0.4095
            self.result_label.setText(f"Masa în kilograme: {kg:.3f}")
        except ValueError:
            self.result_label.setText("Introduceți o valoare numerică pozitivă.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PoundToKgPositive()
    window.show()
    sys.exit(app.exec_())