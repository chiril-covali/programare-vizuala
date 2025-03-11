import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import QTimer
from datetime import datetime

class ClockWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ceas electronic cu dată")
        self.setGeometry(100, 100, 300, 150)
        
        # Create layout
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # Create time label
        self.time_label = QLabel()
        self.time_label.setStyleSheet("font-size: 36px; font-weight: bold;")
        layout.addWidget(self.time_label)
        
        # Create date label
        self.date_label = QLabel()
        self.date_label.setStyleSheet("font-size: 24px; color: #2980b9;")
        layout.addWidget(self.date_label)
        
        # Create and start timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_datetime)
        self.timer.start(1000)  # Update every second
        
        # Initial display
        self.update_datetime()
    
    def update_datetime(self):
        now = datetime.now()
        time_str = now.strftime("%H:%M:%S")
        date_str = now.strftime("%d %B %Y")
        self.time_label.setText(time_str)
        self.date_label.setText(date_str)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ClockWindow()
    window.show()
    sys.exit(app.exec_())