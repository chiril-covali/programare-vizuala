#!/usr/bin/env python3
# coding: utf-8
import sys
import random
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QLineEdit, QPushButton
from PyQt5.QtCore import QTimer

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test Memorie")
        self.layout = QVBoxLayout()
        self.label = QLabel("")
        self.layout.addWidget(self.label)
        # Câmp de input și buton
        self.input_field = QLineEdit()
        self.submit_btn = QPushButton("Submit")
        self.layout.addWidget(self.input_field)
        self.layout.addWidget(self.submit_btn)
        self.input_field.hide()
        self.submit_btn.hide()
        self.setLayout(self.layout)
        # Generăm o listă de 5 numere aleatorii
        self.numbers = [random.randint(0, 99) for _ in range(5)]
        self.current_index = 0
        self.correct_count = 0
        self.submit_btn.clicked.connect(self.check_answer)
        QTimer.singleShot(500, self.next_round)

    def next_round(self):
        self.input_field.clear()
        if self.current_index >= len(self.numbers):
            self.show_result()
            return
        self.input_field.hide()
        self.submit_btn.hide()
        # Afișăm numărul curent
        self.label.setText(str(self.numbers[self.current_index]))
        QTimer.singleShot(1000, self.prompt_input)

    def prompt_input(self):
        self.label.setText("")
        self.input_field.show()
        self.submit_btn.show()
        self.input_field.setFocus()

    def check_answer(self):
        answer = self.input_field.text().strip()
        correct = str(self.numbers[self.current_index])
        if answer == correct:
            self.correct_count += 1
        self.current_index += 1
        self.next_round()

    def show_result(self):
        self.label.setText(f"Test finalizat: A fost afisat {len(self.numbers)} numere, din care corect: {self.correct_count}.")
        self.input_field.hide()
        self.submit_btn.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
