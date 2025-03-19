import sys
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QMessageBox
)
from PyQt5.QtCore import QTimer

class AlarmWindow(QWidget):
    def __init__(self, reminder_text):
        super().__init__()
        self.setWindowTitle("Alarmă")
        layout = QVBoxLayout()
        layout.addWidget(QLabel(reminder_text))
        self.setLayout(layout)
        QApplication.beep()  # Semnal sonor

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ceas de alarmă")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Setați ora alarmei (HH:MM):"))
        self.time_edit = QLineEdit()
        layout.addWidget(self.time_edit)
        layout.addWidget(QLabel("Text de reamintire:"))
        self.reminder_edit = QLineEdit()
        layout.addWidget(self.reminder_edit)
        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.schedule_alarm)
        layout.addWidget(self.ok_button)
        self.setLayout(layout)

    def schedule_alarm(self):
        alarm_time_str = self.time_edit.text().strip()
        reminder_text = self.reminder_edit.text().strip()
        try:
            now = datetime.now()
            alarm_time = datetime.strptime(alarm_time_str, "%H:%M")
            alarm_time = now.replace(hour=alarm_time.hour, minute=alarm_time.minute, second=0, microsecond=0)
            if alarm_time < now:
                alarm_time += timedelta(days=1)
            delay_ms = int((alarm_time - now).total_seconds() * 1000)
        except Exception:
            QMessageBox.critical(self, "Eroare", "Format de oră invalid. Utilizați HH:MM.")
            return
        self.close()  # Închide fereastra principală
        QTimer.singleShot(delay_ms, lambda: self.show_alarm(reminder_text))

    def show_alarm(self, reminder_text):
        self.alarm_win = AlarmWindow(reminder_text)
        self.alarm_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
