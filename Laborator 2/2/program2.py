import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIntValidator

class WindSpeedConverterInt(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Viteza vântului (număr întreg pozitiv)")
        self.init_ui()

    def init_ui(self):
        self.input_label = QLabel("Introduceți viteza (m/s):")
        self.input_edit = QLineEdit()
        self.input_edit.setValidator(QIntValidator(0, 10000, self))
        self.result_label = QLabel("Rezultat (km/h):")
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
            mps = int(self.input_edit.text())
            kmh = mps * 3.6
            self.result_label.setText(f"Rezultat (km/h): {kmh:.2f}")
        except ValueError:
            self.result_label.setText("Introduceți un număr întreg pozitiv.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WindSpeedConverterInt()
    window.show()
    sys.exit(app.exec_())