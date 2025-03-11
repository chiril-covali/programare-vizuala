import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtGui import QPainter, QColor, QPen, QFont
from PyQt5.QtCore import Qt, QTimer, QPoint, QTime, QRect
import math

class ClockDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ceas analogic în dialog')
        self.setFixedSize(300, 350)  # Mărime ajustată pentru a avea loc si ceas digital
        
        # Update timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)  # Update every second
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Calculate clock center and radius
        center = QPoint(self.width() // 2, (self.height() - 50) // 2)  # ajustează pentru spațiu pentru ceas digital
        radius = min(self.width(), self.height() - 50) // 2 - 20
        
        # Draw clock face with numbers
        self.draw_clock_face(painter, center, radius)
        
        # Get current time
        current_time = QTime.currentTime()
        
        # Draw clock hands
        self.draw_hour_hand(painter, center, radius * 0.5, current_time)
        self.draw_minute_hand(painter, center, radius * 0.7, current_time)
        self.draw_second_hand(painter, center, radius * 0.8, current_time)
        
        # Draw center point
        painter.setPen(QPen(Qt.black, 3))
        painter.drawEllipse(center, 5, 5)
        
        # Draw digital clock below the analog clock
        digital_rect = QRect(0, self.height() - 50, self.width(), 50)
        painter.setFont(QFont("Arial", 16))
        painter.drawText(digital_rect, Qt.AlignCenter, current_time.toString("hh:mm:ss"))
        
    def draw_clock_face(self, painter, center, radius):
        # Draw outer circle
        painter.setPen(QPen(Qt.black, 2))
        painter.drawEllipse(center, radius, radius)
        
        # Draw hour marks
        for i in range(12):
            angle = i * 30  # 360 / 12 = 30
            painter.save()
            painter.translate(center)
            painter.rotate(angle)
            painter.drawLine(0, -radius, 0, -radius + 15)
            painter.restore()
        
        # Draw hour numbers
        painter.setFont(QFont("Arial", 10))
        for i in range(1, 13):
            angle = math.radians(i * 30 - 90)
            x = center.x() + int((radius - 25) * math.cos(angle))
            y = center.y() + int((radius - 25) * math.sin(angle))
            num_rect = QRect(x - 10, y - 10, 20, 20)
            painter.drawText(num_rect, Qt.AlignCenter, str(i))
        
    def draw_hour_hand(self, painter, center, length, time):
        angle = (30 * (time.hour() % 12) + time.minute() / 2) * math.pi / 180
        self.draw_hand(painter, center, length, angle, 4)
        
    def draw_minute_hand(self, painter, center, length, time):
        angle = (6 * time.minute() + time.second() / 10) * math.pi / 180
        self.draw_hand(painter, center, length, angle, 3)
        
    def draw_second_hand(self, painter, center, length, time):
        angle = 6 * time.second() * math.pi / 180
        painter.setPen(QPen(Qt.red, 1))
        end_x = center.x() + length * math.sin(angle)
        end_y = center.y() - length * math.cos(angle)
        painter.drawLine(center, QPoint(int(end_x), int(end_y)))
        
    def draw_hand(self, painter, center, length, angle, width):
        painter.setPen(QPen(Qt.black, width))
        end_x = center.x() + length * math.sin(angle)
        end_y = center.y() - length * math.cos(angle)
        painter.drawLine(center, QPoint(int(end_x), int(end_y)))

def main():
    app = QApplication(sys.argv)
    dialog = ClockDialog()
    dialog.exec_()

if __name__ == '__main__':
    main()