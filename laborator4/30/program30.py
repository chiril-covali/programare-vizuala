#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout,
    QTableWidget, QTableWidgetItem, QPushButton, QLabel
)
from PyQt5.QtGui import QPainter, QColor, QPen, QFont
from PyQt5.QtCore import Qt, QRectF

class HistogramWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.data = []  # list of tuples: (label, value)

    def setData(self, data):
        self.data = data
        self.update()  # for repaint

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        rect = self.contentsRect()
        painter.fillRect(rect, QColor("white"))
        
        if not self.data:
            # Mesaj de informare dacă nu există date
            painter.setPen(Qt.black)
            painter.setFont(QFont("Arial", 12))
            painter.drawText(rect, Qt.AlignCenter, "Nu există date pentru histogramă.")
            return
        
        # Calculăm înălțimea maximă din setul de date pentru scalare
        max_value = max([value for label, value in self.data])
        if max_value == 0:
            max_value = 1
        
        # Setăm margini și spațiu între bare
        margin = 20
        spacing = 10
        available_width = rect.width() - 2 * margin
        available_height = rect.height() - 2 * margin
        n = len(self.data)
        bar_width = (available_width - (n - 1) * spacing) / n

        # Desenăm fiecare bară
        for idx, (label, value) in enumerate(self.data):
            # Calculăm înălțimea barei
            bar_height = (value / max_value) * available_height
            x = margin + idx * (bar_width + spacing)
            y = rect.height() - margin - bar_height

            # Desenăm bara
            bar_rect = QRectF(x, y, bar_width, bar_height)
            painter.setPen(QPen(Qt.black, 1))
            painter.setBrush(QColor("skyblue"))
            painter.drawRect(bar_rect)

            # Etichetă sub bară
            painter.setPen(Qt.black)
            painter.setFont(QFont("Arial", 10))
            label_text = str(label)
            text_rect = QRectF(x, rect.height() - margin, bar_width, margin)
            painter.drawText(text_rect, Qt.AlignHCenter | Qt.AlignTop, label_text)

            # Valoare deasupra barei
            value_text = str(value)
            value_rect = QRectF(x, y - margin/2, bar_width, margin/2)
            painter.drawText(value_rect, Qt.AlignHCenter | Qt.AlignBottom, value_text)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Histogramă și Tabel de Date")
        self.resize(800, 600)
        
        # Widget-ul central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal orizontal
        main_layout = QHBoxLayout(central_widget)
        
        # Histogramă pe partea stângă
        self.histogram_widget = HistogramWidget()
        main_layout.addWidget(self.histogram_widget, 2)
        
        # Panou din dreapta: tabel cu date și buton
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        main_layout.addWidget(right_panel, 1)
        
        # Tabelul cu date (ex: rezultate test)
        self.table = QTableWidget(0, 2)
        self.table.setHorizontalHeaderLabels(["Test", "Scor"])
        right_layout.addWidget(self.table)
        
        # Exemplu de date: Adăugăm câteva rânduri pentru testare
        sample_data = [
            ("Test 1", 75),
            ("Test 2", 85),
            ("Test 3", 60),
            ("Test 4", 90),
            ("Test 5", 55)
        ]
        self.addSampleData(sample_data)
        
        # Butonul pentru creare histogramă
        self.create_button = QPushButton("Creează Histogramă")
        self.create_button.clicked.connect(self.createHistogram)
        right_layout.addWidget(self.create_button)

    def addSampleData(self, data):
        # Adăugăm date în tabel
        self.table.setRowCount(len(data))
        for row, (test, score) in enumerate(data):
            test_item = QTableWidgetItem(test)
            score_item = QTableWidgetItem(str(score))
            self.table.setItem(row, 0, test_item)
            self.table.setItem(row, 1, score_item)

    def createHistogram(self):
        # Extragem datele din tabel
        data = []
        row_count = self.table.rowCount()
        for row in range(row_count):
            label_item = self.table.item(row, 0)
            score_item = self.table.item(row, 1)
            if label_item is not None and score_item is not None:
                try:
                    value = float(score_item.text())
                except ValueError:
                    value = 0
                data.append((label_item.text(), value))
        # Setăm datele în widget-ul histogramă
        self.histogram_widget.setData(data)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())