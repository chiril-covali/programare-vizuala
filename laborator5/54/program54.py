#!/usr/bin/env python3
# coding: utf-8
import sys, random, os
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QVBoxLayout, QMessageBox, QLabel, QHBoxLayout, QScrollArea, QFileDialog
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QSize

class PuzzleGame(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Asamblează imaginea")
        self.resize(300, 300)  # fereastra redimensionată mai mic (anterior 500, 500)
        main_layout = QVBoxLayout()
        # Buton pentru a vedea imaginea originală
        btn_show = QPushButton("Deschide imaginea")
        btn_show.clicked.connect(self.show_original)
        main_layout.addWidget(btn_show)
        
        # Nou: buton pentru a încărca o altă imagine
        btn_load = QPushButton("Încarcă imagine")
        btn_load.clicked.connect(self.load_image)
        main_layout.addWidget(btn_load)
        
        # Grila pentru puzzle
        self.grid = QGridLayout()
        main_layout.addLayout(self.grid)
        self.setLayout(main_layout)
        
        self.image_path = "puzzle.png"  # imaginea de încărcat implicit
        if not os.path.exists(self.image_path):
            QMessageBox.critical(self, "Eroare", f"Nu s-a găsit fișierul {self.image_path}")
            sys.exit(1)
        
        self.full_image = QPixmap(self.image_path)
        self.split_image()
        self.setup_buttons()
    
    def split_image(self):
        # Împarte imaginea în 16 fragmente
        self.rows = self.cols = 4
        self.piece_width = self.full_image.width() // self.cols
        self.piece_height = self.full_image.height() // self.rows
        # Creează lista de fragmente
        pieces = []
        for i in range(self.rows):
            for j in range(self.cols):
                rect = (j * self.piece_width, i * self.piece_height, self.piece_width, self.piece_height)
                pieces.append(self.full_image.copy(*rect))
        # Ultimul element devine celulă goală
        pieces[-1] = None
        # Amestecă fragmentele 
        random.shuffle(pieces)
        # Organizează matricea de puzzle
        self.board = []
        index = 0
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(pieces[index])
                if pieces[index] is None:
                    self.empty_pos = (i, j)
                index += 1
            self.board.append(row)
    
    def setup_buttons(self):
        # Ștergere widgeturi anterioare din grilă
        while self.grid.count():
            widget = self.grid.takeAt(0).widget()
            if widget:
                widget.deleteLater()
        self.buttons = {}
        for i in range(self.rows):
            for j in range(self.cols):
                btn = QPushButton()
                btn.setFixedSize(self.piece_width, self.piece_height)
                piece = self.board[i][j]
                if piece:
                    btn.setIcon(QIcon(piece))
                    btn.setIconSize(QSize(self.piece_width, self.piece_height))
                else:
                    btn.setText("")
                btn.clicked.connect(self.make_move(i, j))
                self.grid.addWidget(btn, i, j)
                self.buttons[(i, j)] = btn
    
    def make_move(self, i, j):
        def handler():
            # Verifică dacă celula (i, j) este adiacentă celulei goale
            ei, ej = self.empty_pos
            if (abs(i - ei) == 1 and j == ej) or (abs(j - ej) == 1 and i == ei):
                # Mută piesa
                self.board[ei][ej], self.board[i][j] = self.board[i][j], self.board[ei][ej]
                self.empty_pos = (i, j)
                self.setup_buttons()
                self.check_win()
        return handler
    
    def check_win(self):
        # Verifică ordonarea corectă a pieselor
        correct = []
        for i in range(self.rows):
            for j in range(self.cols):
                rect = (j * self.piece_width, i * self.piece_height, self.piece_width, self.piece_height)
                correct.append(self.full_image.copy(*rect))
        # În board, ultimul trebuie să fie None
        flat_board = [piece for row in self.board for piece in row]
        for idx in range(len(flat_board)-1):
            piece = flat_board[idx]
            ref = correct[idx]
            if piece is None or piece.size() != ref.size():
                return
        QMessageBox.information(self, "Felicitări!", "Ai reușit să asamblezi imaginea!")
    
    def show_original(self):
        # Deschide o fereastră nouă ce afișează imaginea originală
        self.win = QWidget()
        self.win.setWindowTitle("Imaginea originală")
        layout = QVBoxLayout()
        label = QLabel()
        label.setPixmap(self.full_image)
        scroll = QScrollArea()
        scroll.setWidget(label)
        layout.addWidget(scroll)
        self.win.setLayout(layout)
        self.win.resize(600, 600)
        self.win.show()
    
    def load_image(self):
        # Deschide un dialog pentru a selecta o imagine nouă
        file_path, _ = QFileDialog.getOpenFileName(self, "Deschide imagine", "", "Imagini (*.png *.jpg *.jpeg *.bmp)")
        if file_path:
            self.image_path = file_path
            self.full_image = QPixmap(self.image_path)
            self.split_image()
            self.setup_buttons()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PuzzleGame()
    window.show()
    sys.exit(app.exec_())
