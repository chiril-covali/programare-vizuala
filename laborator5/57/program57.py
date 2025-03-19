#!/usr/bin/env python3
# coding: utf-8
import sys, random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import QTimer

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Memorizează numere")
        self.level = 4  # număr de cifre
        self.correct_count = 0
        self.threshold = 3  # prag pentru avansarea nivelului
        self.number_to_remember = ""
        
        self.layout = QVBoxLayout()
        self.number_label = QLabel("")
        self.layout.addWidget(self.number_label)
        self.input_field = QLineEdit()
        self.layout.addWidget(self.input_field)
        self.submit_button = QPushButton("Verifică")
        self.submit_button.clicked.connect(self.check_answer)
        self.layout.addWidget(self.submit_button)
        self.status_label = QLabel("")
        self.layout.addWidget(self.status_label)
        self.setLayout(self.layout)
        self.new_round()

    def new_round(self):
        # generează un număr aleator cu numărul actual de cifre
        self.number_to_remember = "".join(random.choice("0123456789") for _ in range(self.level))
        self.status_label.setText(f"Nivel: {self.level} | Răspunsuri corecte: {self.correct_count}/{self.threshold}")
        self.number_label.setText(self.number_to_remember)
        self.input_field.clear()
        self.input_field.setEnabled(False)
        self.submit_button.setEnabled(False)
        # ascunde numărul după 2 secunde
        QTimer.singleShot(2000, self.hide_number)

    def hide_number(self):
        self.number_label.setText("...")
        self.input_field.setEnabled(True)
        self.input_field.setFocus()
        self.submit_button.setEnabled(True)

    def check_answer(self):
        answer = self.input_field.text()
        if answer == self.number_to_remember:
            self.correct_count += 1
            self.status_label.setText("Corect! " + f"Nivel: {self.level} | Răspunsuri corecte: {self.correct_count}/{self.threshold}")
            if self.correct_count >= self.threshold:
                self.level += 1
                self.correct_count = 0
                self.status_label.setText("Nivel crescut! Acum nivel: " + str(self.level))
        else:
            self.status_label.setText("Greșit! " + f"Nivel: {self.level} | Răspunsuri corecte: {self.correct_count}/{self.threshold}")
        self.new_round()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
