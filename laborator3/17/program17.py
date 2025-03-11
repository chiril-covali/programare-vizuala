import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import QTimer
from datetime import datetime

class ClockWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ceas electronic")
        self.setGeometry(100, 100, 250, 100)
        
        # Create layout
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # Create time label
        self.time_label = QLabel()
        self.time_label.setStyleSheet("font-size: 36px; font-weight: bold;")
        layout.addWidget(self.time_label)
        
        # Create and start timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Update every second
        
        # Initial time display
        self.update_time()
    
    def update_time(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        self.time_label.setText(current_time)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ClockWindow()
    window.show()
    sys.exit(app.exec_())