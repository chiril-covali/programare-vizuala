import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QMessageBox

class Game15(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Jocul 15")
        self.resize(320, 320)  # adăugat pentru a face fereastra mai mică
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.buttons = {}
        self.empty_pos = (3, 3)
        self.init_board()
    
    def init_board(self):
        # Creează lista de numere (1-15) plus spațiul gol (0) și le amestecă
        numbers = list(range(1, 16)) + [0]
        random.shuffle(numbers)
        self.board = []
        for i in range(4):
            row = numbers[i*4:(i+1)*4]
            self.board.append(row)
        # Determină poziția goală
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == 0:
                    self.empty_pos = (i, j)
        self.setup_buttons()
    
    def setup_buttons(self):
        # Golește grila înainte de a reconfigura butoanele
        while self.grid.count():
            widget = self.grid.takeAt(0).widget()
            if widget:
                widget.deleteLater()
        for i in range(4):
            for j in range(4):
                num = self.board[i][j]
                btn = QPushButton(str(num) if num != 0 else "")
                btn.setFixedSize(80, 80)
                btn.clicked.connect(self.make_move(i, j))
                self.grid.addWidget(btn, i, j)
                self.buttons[(i, j)] = btn
    
    def make_move(self, i, j):
        def handler():
            # Verifică dacă poziția selectată este adiacentă celulei goale
            if (abs(i - self.empty_pos[0]) == 1 and j == self.empty_pos[1]) or \
               (abs(j - self.empty_pos[1]) == 1 and i == self.empty_pos[0]):
                # Schimbă pozițiile
                self.board[self.empty_pos[0]][self.empty_pos[1]], self.board[i][j] = self.board[i][j], self.board[self.empty_pos[0]][self.empty_pos[1]]
                self.empty_pos = (i, j)
                self.setup_buttons()
                self.check_win()
        return handler
    
    def check_win(self):
        # Verifică dacă jetoanele sunt aliniate în ordine (exclus spațiul gol din verificare)
        nums = []
        for i in range(4):
            nums.extend(self.board[i])
        if nums[:-1] == list(range(1, 16)):
            QMessageBox.information(self, "Felicitări!", "Ai câștigat jocul!")
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Game15()
    window.show()
    sys.exit(app.exec_())
