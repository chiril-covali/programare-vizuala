#!/usr/bin/env python3
# coding: utf-8
import sys
from PyQt5.QtWidgets import QApplication, QTextEdit, QWidget, QVBoxLayout, QPushButton, QFileDialog

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Program 50 - Afiseaza Text")
        layout = QVBoxLayout()
        # Buton de deschidere fisier
        self.openButton = QPushButton("Deschide fisier")
        self.openButton.clicked.connect(self.open_file)
        layout.addWidget(self.openButton)
        # Creează câmpul Memo
        self.memo = QTextEdit()
        self.memo.setReadOnly(True)
        layout.addWidget(self.memo)
        self.setLayout(layout)

    def open_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, "Selecteaza fisierul text", "", "Text Files (*.txt);;All Files (*)", options=options)
        if filename:
            try:
                with open(filename, "r", encoding="utf-8") as f:
                    content = f.read()
            except Exception as e:
                content = f"Nu s-a putut incarca fisierul: {e}"
            self.memo.setText(content)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
