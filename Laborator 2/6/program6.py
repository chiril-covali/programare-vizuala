import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout
from PyQt5.QtGui import QIntValidator, QDoubleValidator

class RunnerSpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calcul Viteza Alergătorului")
        self.init_ui()

    def init_ui(self):
        self.distance_label = QLabel("Distanța parcursă (km):")
        self.distance_edit = QLineEdit()
        self.minutes_label = QLabel("Minute:")
        self.minutes_edit = QLineEdit()
        self.minutes_edit.setValidator(QIntValidator(0, 10000, self))
        self.seconds_label = QLabel("Secunde:")
        self.seconds_edit = QLineEdit()
        self.seconds_edit.setValidator(QDoubleValidator(0.0, 60.0, 2, self))
        self.result_label = QLabel("Viteza (km/h):")
        self.calculate_btn = QPushButton("Calculează")
        self.calculate_btn.clicked.connect(self.calculate)
        
        layout = QGridLayout()
        layout.addWidget(self.distance_label, 0, 0)
        layout.addWidget(self.distance_edit, 0, 1)
        layout.addWidget(self.minutes_label, 1, 0)
        layout.addWidget(self.minutes_edit, 1, 1)
        layout.addWidget(self.seconds_label, 2, 0)
        layout.addWidget(self.seconds_edit, 2, 1)
        layout.addWidget(self.calculate_btn, 3, 0, 1, 2)
        layout.addWidget(self.result_label, 4, 0, 1, 2)
        
        self.setLayout(layout)

    def calculate(self):
        try:
            distance = float(self.distance_edit.text())
            minutes = int(self.minutes_edit.text())
            seconds = float(self.seconds_edit.text())
            total_time_hours = (minutes + seconds/60) / 60
            if total_time_hours == 0:
                self.result_label.setText("Timpul nu poate fi 0.")
                return
            speed = distance / total_time_hours
            self.result_label.setText(f"Viteza (km/h): {speed:.2f}")
        except ValueError:
            self.result_label.setText("Introduceți valori numerice valide.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RunnerSpeedCalculator()
    window.show()
    sys.exit(app.exec_())