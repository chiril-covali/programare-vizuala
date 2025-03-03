import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class PoundToKgRawInput(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Livre în Kilograme - Activare Buton")
        self.init_ui()

    def init_ui(self):
        self.input_label = QLabel("Introduceți masa (lire):")
        self.input_edit = QLineEdit()
        self.input_edit.textChanged.connect(self.enable_button)
        self.result_label = QLabel("Masa în kilograme:")
        self.calculate_btn = QPushButton("Recalculare")
        self.calculate_btn.setEnabled(False)
        self.calculate_btn.clicked.connect(self.calculate)
        
        layout = QVBoxLayout()
        layout.addWidget(self.input_label)
        layout.addWidget(self.input_edit)
        layout.addWidget(self.calculate_btn)
        layout.addWidget(self.result_label)
        self.setLayout(layout)
    
    def enable_button(self, text):
        self.calculate_btn.setEnabled(bool(text.strip()))
    
    def calculate(self):
        try:
            lb = float(self.input_edit.text())
            kg = lb * 0.4095  # deoarece 409,5 grame = 0.4095 kg
            self.result_label.setText(f"Masa în kilograme: {kg:.3f}")
        except ValueError:
            self.result_label.setText("Introduceți o valoare numerică.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PoundToKgRawInput()
    window.show()
    sys.exit(app.exec_())