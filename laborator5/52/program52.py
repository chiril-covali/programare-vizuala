#!/usr/bin/env python3
# coding: utf-8
import sys
import os
import random
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QCalendarWidget, QLineEdit, QPushButton

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.check_weather_file()  # Verifică și creează Weather.txt dacă nu există
        self.setWindowTitle("Program 52")
        # Layout principal orizontal
        main_layout = QHBoxLayout()
        
        # Widgetul calendar (stanga)
        self.calendar = QCalendarWidget()
        self.calendar.clicked.connect(self.on_date_clicked)  # conexiune nouă la eveniment
        main_layout.addWidget(self.calendar)
        
        # Containerul pentru temperatura si butoane (dreapta)
        right_widget = QWidget()
        right_layout = QVBoxLayout()
        right_layout.addWidget(QLabel("Temperatura:"))
        self.temp_input = QLineEdit()
        right_layout.addWidget(self.temp_input)
        
        # Buton pentru adăugare înregistrare
        btn_add = QPushButton("Adaugă")
        btn_add.clicked.connect(self.add_record)
        right_layout.addWidget(btn_add)
        
        right_widget.setLayout(right_layout)
        main_layout.addWidget(right_widget)
        
        self.setLayout(main_layout)
        self.resize(400, 300)  # fereastra redimensionată mai mic (anterior 500, 400)
    
    def check_weather_file(self):
        if not os.path.exists("Weather.txt"):
            with open("Weather.txt", "w", encoding="utf-8") as f:
                f.write("")  # creează un fișier gol
    
    def add_record(self):
        # Extrage data și temperatura
        date = self.calendar.selectedDate().toString("yyyy-MM-dd")
        temp = self.temp_input.text()
        if temp:
            # Deschide sau creează fișierul Weather.txt în modul append
            with open("Weather.txt", "a", encoding="utf-8") as f:
                f.write(f"{date} {temp}\n")
    
    def on_date_clicked(self, date):
        date_str = date.toString("yyyy-MM-dd")
        temperature = None
        # Citește linie cu linie pentru a găsi înregistrarea corespunzătoare datei
        with open("Weather.txt", "r", encoding="utf-8") as f:
            for line in f:
                # presupunem că fiecare linie începe cu data în formatul yyyy-MM-dd
                if line.startswith(date_str):
                    parts = line.strip().split()
                    if len(parts) >= 2:
                        temperature = parts[1]
        if temperature:
            self.temp_input.setText(f"{temperature} grade")
        else:
            self.temp_input.clear()
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
