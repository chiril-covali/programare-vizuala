import sys
import random
from PyQt5 import QtWidgets, QtCore

class CellButton(QtWidgets.QPushButton):
    def __init__(self, x, y, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pos_x = x
        self.pos_y = y
        self.is_mine = False
        self.is_revealed = False
        self.is_flagged = False
        self.adjacent_mines = 0
        self.setFixedSize(30, 30)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.RightButton:
            self.toggle_flag()
        else:
            self.reveal()
        super().mousePressEvent(event)

    def toggle_flag(self):
        if not self.is_revealed:
            self.is_flagged = not self.is_flagged
            if self.is_flagged:
                self.setText("F")
                self.setStyleSheet("background-color: orange;")
            else:
                self.setText("")
                self.setStyleSheet("")

    def reveal(self):
        if self.is_revealed or self.is_flagged: 
            return
        self.is_revealed = True
        if self.is_mine:
            self.setText("M")
            self.setStyleSheet("background-color: red;")
            self.window().game_over()  # Updated call
        else:
            if self.adjacent_mines > 0:
                self.setText(str(self.adjacent_mines))
            self.setStyleSheet("background-color: lightgrey;")
            if self.adjacent_mines == 0:
                self.window().reveal_adjacent(self.pos_x, self.pos_y)

class SapperGame(QtWidgets.QMainWindow):
    def __init__(self, rows=10, cols=10, mines_count=10):
        super().__init__()
        self.rows = rows
        self.cols = cols
        self.mines_count = mines_count
        self.initUI()

    def initUI(self):
        self.centralWidget = QtWidgets.QWidget()
        self.setCentralWidget(self.centralWidget)
        self.grid = QtWidgets.QGridLayout(self.centralWidget)

        self.cells = {}
        for x in range(self.rows):
            for y in range(self.cols):
                btn = CellButton(x, y)
                btn.setParent(self)
                self.grid.addWidget(btn, x, y)
                self.cells[(x, y)] = btn

        self.place_mines()
        self.calculate_adjacency()
        self.setWindowTitle("Căutătorul de mine (Sapper)")
        self.show()

    def place_mines(self):
        positions = random.sample(list(self.cells.keys()), self.mines_count)
        for pos in positions:
            self.cells[pos].is_mine = True

    def calculate_adjacency(self):
        for (x, y), cell in self.cells.items():
            if cell.is_mine:
                continue
            count = 0
            for i in range(max(0, x - 1), min(self.rows, x + 2)):
                for j in range(max(0, y - 1), min(self.cols, y + 2)):
                    if self.cells[(i, j)].is_mine:
                        count += 1
            cell.adjacent_mines = count

    def reveal_adjacent(self, x, y):
        for i in range(max(0, x - 1), min(self.rows, x + 2)):
            for j in range(max(0, y - 1), min(self.cols, y + 2)):
                if (i, j) != (x, y):
                    neighbor = self.cells[(i, j)]
                    if not neighbor.is_revealed and not neighbor.is_mine:
                        neighbor.reveal()

    def game_over(self):
        for cell in self.cells.values():
            if cell.is_mine:
                cell.setText("M")
                cell.setStyleSheet("background-color: red;")
        msg = QtWidgets.QMessageBox()
        msg.setText("Game Over!")
        msg.exec_()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = SapperGame(10, 10, 10)
    sys.exit(app.exec_())