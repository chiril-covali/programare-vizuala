import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget,
    QFileDialog, QInputDialog
)
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtCore import Qt, QTimer, QRect

class BMPAnimatedViewerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Desen animat BMP - Frame by Frame')
        self.setGeometry(100, 100, 800, 600)
        
        # Widget central și layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Adăugăm un stretch pentru a împinge butonul în partea de jos.
        layout.addStretch()
        
        # Buton pentru încărcarea imaginii BMP animat
        self.load_button = QPushButton('Încarcă BMP animat', self)
        self.load_button.clicked.connect(self.load_image)
        layout.addWidget(self.load_button)
        
        self.sprite_sheet = None  # imaginea BMP care conține cadre
        self.frame_count = 0
        self.frame_index = 0
        
        # Timer pentru animație (schimbă cadrul la interval constant)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(100)  # actualizează la fiecare 100ms
        
    def load_image(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            'Selectați fișierul BMP animat',
            '',
            'BMP Files (*.bmp)'
        )
        
        if file_name:
            self.sprite_sheet = QPixmap(file_name)
            # Solicită numărul de cadre din sprite sheet
            count, ok = QInputDialog.getInt(
                self, "Număr de cadre",
                "Introduceți numărul de cadre din desenul animat:",
                min=1, value=2
            )
            if ok:
                self.frame_count = count
                self.frame_index = 0
            self.update()
    
    def update_frame(self):
        if self.sprite_sheet and self.frame_count:
            # Incrementează și ciclizează indexul cadrului
            self.frame_index = (self.frame_index + 1) % self.frame_count
            self.update()
            
    def paintEvent(self, event):
        if self.sprite_sheet and self.frame_count:
            painter = QPainter(self)
            
            frame_width = self.sprite_sheet.width() // self.frame_count
            frame_height = self.sprite_sheet.height()
            # Obține cadrul curent din sprite sheet
            current_frame = self.sprite_sheet.copy(
                self.frame_index * frame_width, 0,
                frame_width, frame_height
            )
            
            # Centrează cadrul în fereastră
            x = (self.width() - frame_width) // 2
            y = (self.height() - frame_height) // 2
            painter.drawPixmap(x, y, current_frame)

def main():
    app = QApplication(sys.argv)
    window = BMPAnimatedViewerWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()