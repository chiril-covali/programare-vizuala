import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtGui import QDoubleValidator

class CurrentCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calcul Curent (V=220V)")
        self.init_ui()

    def init_ui(self):
        self.res_label = QLabel("Introduceți rezistența (ohmi):")
        self.res_edit = QLineEdit()
        validator = QDoubleValidator(0.0, 1e6, 2, self)
        self.res_edit.setValidator(validator)
        self.res_edit.textChanged.connect(self.enable_button)
        self.calculate_btn = QPushButton("Calculare")
        self.calculate_btn.setEnabled(False)
        self.calculate_btn.clicked.connect(self.calculate)
        self.result_label = QLabel("Curentul (A):")
        
        layout = QVBoxLayout()
        layout.addWidget(self.res_label)
        layout.addWidget(self.res_edit)
        layout.addWidget(self.calculate_btn)
        layout.addWidget(self.result_label)
        self.setLayout(layout)
    
    def enable_button(self, text):
        self.calculate_btn.setEnabled(bool(text.strip()))
    
    def calculate(self):
        try:
            R = float(self.res_edit.text())
            if R == 0:
                self.result_label.setText("Rezistența nu poate fi 0.")
                return
            I = 220 / R
            self.result_label.setText(f"Curentul (A): {I:.2f}")
        except ValueError:
            self.result_label.setText("Introduceți o valoare numerică.")
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CurrentCalculator()
    window.show()
    sys.exit(app.exec_())