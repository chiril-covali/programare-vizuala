import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout,
                             QHBoxLayout, QWidget, QFileDialog, QLabel)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os

class ImageViewerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Vizualizator de imagini')
        self.setGeometry(100, 100, 800, 600)
        
        # Create central widget and layouts
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        button_layout = QHBoxLayout()
        
        # Create buttons
        self.select_dir_button = QPushButton('Selectează director', self)
        self.prev_button = QPushButton('Anterior', self)
        self.next_button = QPushButton('Următor', self)
        
        # Add buttons to layout
        button_layout.addWidget(self.select_dir_button)
        button_layout.addWidget(self.prev_button)
        button_layout.addWidget(self.next_button)
        main_layout.addLayout(button_layout)
        
        # Create image label
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.image_label)
        
        # Connect buttons
        self.select_dir_button.clicked.connect(self.select_directory)
        self.prev_button.clicked.connect(self.show_previous_image)
        self.next_button.clicked.connect(self.show_next_image)
        
        # Initialize variables
        self.current_dir = ''
        self.image_files = []
        self.current_index = -1
        
        # Disable navigation buttons initially
        self.prev_button.setEnabled(False)
        self.next_button.setEnabled(False)
        
    def select_directory(self):
        directory = QFileDialog.getExistingDirectory(self, 'Selectează director')
        if directory:
            self.current_dir = directory
            self.load_images()
            
    def load_images(self):
        # Get all image files from directory (considerăm ilustrații ca fiind fișiere cu extensii comune)
        self.image_files = [
            f for f in os.listdir(self.current_dir)
            if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))
        ]
        
        if self.image_files:
            self.current_index = 0
            self.show_current_image()
            self.update_button_states()
        
    def show_current_image(self):
        if 0 <= self.current_index < len(self.image_files):
            image_path = os.path.join(self.current_dir, self.image_files[self.current_index])
            pixmap = QPixmap(image_path)
            
            # Scale pixmap to fit the label while maintaining aspect ratio
            scaled_pixmap = pixmap.scaled(
                self.image_label.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            self.image_label.setPixmap(scaled_pixmap)
            
    def show_previous_image(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.show_current_image()
            self.update_button_states()
            
    def show_next_image(self):
        if self.current_index < len(self.image_files) - 1:
            self.current_index += 1
            self.show_current_image()
            self.update_button_states()
            
    def update_button_states(self):
        self.prev_button.setEnabled(self.current_index > 0)
        self.next_button.setEnabled(self.current_index < len(self.image_files) - 1)
        
    def resizeEvent(self, event):
        super().resizeEvent(event)
        if self.image_label.pixmap():
            self.show_current_image()

def main():
    app = QApplication(sys.argv)
    window = ImageViewerWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()