import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QSpinBox
from PyQt5.QtCore import QTimer

class TimerWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Timer")
        self.setGeometry(100, 100, 300, 200)
        
        # Create layout
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # Create time input spinbox
        self.time_input = QSpinBox()
        self.time_input.setRange(1, 3600)  # 1 second to 1 hour
        self.time_input.setSuffix(" secunde")
        layout.addWidget(self.time_input)
        
        # Create control buttons
        self.start_button = QPushButton("Start")
        self.stop_button = QPushButton("Stop")
        self.stop_button.setEnabled(False)
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)
        
        # Create time display label
        self.time_label = QLabel("00:00")
        self.time_label.setStyleSheet("font-size: 48px; font-weight: bold;")
        layout.addWidget(self.time_label)
        
        # Create timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        
        # Connect buttons
        self.start_button.clicked.connect(self.start_timer)
        self.stop_button.clicked.connect(self.stop_timer)
        
        self.remaining_time = 0
    
    def start_timer(self):
        self.remaining_time = self.time_input.value()
        self.timer.start(1000)  # Update every second
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        self.time_input.setEnabled(False)
        self.update_display()
    
    def stop_timer(self):
        self.timer.stop()
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.time_input.setEnabled(True)
        self.time_label.setText("00:00")
    
    def update_timer(self):
        self.remaining_time -= 1
        if self.remaining_time <= 0:
            self.stop_timer()
        else:
            self.update_display()
    
    def update_display(self):
        minutes = self.remaining_time // 60
        seconds = self.remaining_time % 60
        self.time_label.setText(f"{minutes:02d}:{seconds:02d}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TimerWindow()
    window.show()
    sys.exit(app.exec_())