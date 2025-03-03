import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
                             QPushButton, QVBoxLayout, QRadioButton, QButtonGroup)
from PyQt5.QtGui import QDoubleValidator

class OhmsLawCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator Legea lui Ohm")
        self.init_ui()
        
    def init_ui(self):
        # Opțiuni de calcul
        self.radio_current = QRadioButton("Calculează Curentul (I)")
        self.radio_voltage = QRadioButton("Calculează Tensiunea (V)")
        self.radio_resistance = QRadioButton("Calculează Rezistența (R)")
        self.radio_current.setChecked(True)
        
        self.radio_group = QButtonGroup()
        self.radio_group.addButton(self.radio_current)
        self.radio_group.addButton(self.radio_voltage)
        self.radio_group.addButton(self.radio_resistance)
        
        # Etichetă de descriere (se va actualiza)
        self.desc_label = QLabel("Introduceți V și R:")
        
        self.input1_label = QLabel("Tensiune (V):")
        self.input1_edit = QLineEdit()
        self.input1_edit.setValidator(QDoubleValidator(0.0, 1e6, 2))
        
        self.input2_label = QLabel("Rezistență (ohmi):")
        self.input2_edit = QLineEdit()
        self.input2_edit.setValidator(QDoubleValidator(0.0, 1e6, 2))
        
        self.calculate_btn = QPushButton("Calculează")
        self.calculate_btn.clicked.connect(self.calculate)
        
        self.result_label = QLabel("Rezultat:")
        
        self.radio_current.toggled.connect(self.update_labels)
        self.radio_voltage.toggled.connect(self.update_labels)
        self.radio_resistance.toggled.connect(self.update_labels)
        
        layout = QVBoxLayout()
        layout.addWidget(self.radio_current)
        layout.addWidget(self.radio_voltage)
        layout.addWidget(self.radio_resistance)
        layout.addWidget(self.desc_label)
        layout.addWidget(self.input1_label)
        layout.addWidget(self.input1_edit)
        layout.addWidget(self.input2_label)
        layout.addWidget(self.input2_edit)
        layout.addWidget(self.calculate_btn)
        layout.addWidget(self.result_label)
        self.setLayout(layout)
        
    def update_labels(self):
        if self.radio_current.isChecked():
            self.desc_label.setText("Calcul pentru Curent: Introduceți Tensiunea (V) și Rezistența (ohmi)")
            self.input1_label.setText("Tensiune (V):")
            self.input2_label.setText("Rezistență (ohmi):")
        elif self.radio_voltage.isChecked():
            self.desc_label.setText("Calcul pentru Tensiune: Introduceți Curentul (A) și Rezistența (ohmi)")
            self.input1_label.setText("Curent (A):")
            self.input2_label.setText("Rezistență (ohmi):")
        elif self.radio_resistance.isChecked():
            self.desc_label.setText("Calcul pentru Rezistență: Introduceți Tensiunea (V) și Curentul (A)")
            self.input1_label.setText("Tensiune (V):")
            self.input2_label.setText("Curent (A):")
            
    def calculate(self):
        try:
            if self.radio_current.isChecked():
                V = float(self.input1_edit.text())
                R = float(self.input2_edit.text())
                if R == 0:
                    self.result_label.setText("Rezistența nu poate fi 0.")
                    return
                I = V / R
                self.result_label.setText(f"Curent (I): {I:.2f} A")
            elif self.radio_voltage.isChecked():
                I = float(self.input1_edit.text())
                R = float(self.input2_edit.text())
                V = I * R
                self.result_label.setText(f"Tensiune (V): {V:.2f} V")
            elif self.radio_resistance.isChecked():
                V = float(self.input1_edit.text())
                I = float(self.input2_edit.text())
                if I == 0:
                    self.result_label.setText("Curentul nu poate fi 0.")
                    return
                R = V / I
                self.result_label.setText(f"Rezistență (R): {R:.2f} ohmi")
        except Exception:
            self.result_label.setText("Eroare la calcul.")
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OhmsLawCalculator()
    window.show()
    sys.exit(app.exec_())