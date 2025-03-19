#!/usr/bin/env python3
# coding: utf-8
import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QVBoxLayout, QFileDialog
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QTimer

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pair Pics")
        # Buton pentru deschiderea imaginii dorite
        load_btn = QPushButton("Deschide imagine")
        load_btn.clicked.connect(self.open_image)
        
        # Încarcă sprite-ul implicit
        self.sprite = QPixmap("/Users/covali/Desktop/programare-vizuala-main/sprite.png")
        self.sprite_width = self.sprite.width() // 8
        self.sprite_height = self.sprite.height()
        self.images = [self.sprite.copy(i * self.sprite_width, 0, self.sprite_width, self.sprite_height)
                       for i in range(8)]
        self.cards = self.images * 2
        random.shuffle(self.cards)
        self.buttons = {}
        self.first_selection = None
        self.lock = False

        # Construim tabla ca o grilă 4x4
        self.grid = QGridLayout()
        index = 0
        for row in range(4):
            for col in range(4):
                btn = QPushButton()
                btn.setFixedSize(self.sprite_width, self.sprite_height)
                btn.setIconSize(btn.size())
                btn.setProperty("revealed", False)
                btn.clicked.connect(self.make_flip_handler(btn, index))
                self.buttons[btn] = index
                self.grid.addWidget(btn, row, col)
                index += 1

        # Layout principal cu butonul de încărcare și grila
        main_layout = QVBoxLayout()
        main_layout.addWidget(load_btn)
        main_layout.addLayout(self.grid)
        self.setLayout(main_layout)

    def open_image(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Selectează imaginea", "", "Images (*.png *.jpg *.bmp)")
        if filename:
            self.sprite = QPixmap(filename)
            self.sprite_width = self.sprite.width() // 8
            self.sprite_height = self.sprite.height()
            self.images = [self.sprite.copy(i * self.sprite_width, 0, self.sprite_width, self.sprite_height)
                           for i in range(8)]
            self.cards = self.images * 2
            random.shuffle(self.cards)
            # Resetează butoanele pentru noul sprite
            for btn, idx in self.buttons.items():
                btn.setFixedSize(self.sprite_width, self.sprite_height)
                btn.setIconSize(btn.size())
                btn.setIcon(QIcon())
                btn.setEnabled(True)
                btn.setProperty("revealed", False)
            self.first_selection = None
            self.lock = False

    def make_flip_handler(self, btn, index):
        def handler():
            if self.lock or btn.property("revealed"):
                return
            btn.setIcon(QIcon(self.cards[index]))
            btn.setProperty("revealed", True)
            if self.first_selection is None:
                self.first_selection = (btn, index)
            else:
                first_btn, first_index = self.first_selection  # capture first selection
                second_btn, second_index = btn, index
                self.first_selection = None
                # Dacă imaginile se potrivesc, ascunde butoanele aferente
                if first_index % 8 == second_index % 8:
                    first_btn.hide()
                    second_btn.hide()
                else:
                    self.lock = True
                    QTimer.singleShot(1000, lambda: self.hide_cards(first_btn, second_btn))
        return handler

    def hide_cards(self, btn1, btn2):
        btn1.setIcon(QIcon())
        btn2.setIcon(QIcon())
        btn1.setProperty("revealed", False)
        btn2.setProperty("revealed", False)
        self.lock = False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
