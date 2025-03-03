import tkinter as tk
from tkinter import ttk

class RunnerSpeedCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calcul Viteza Alergătorului")
        self.init_ui()

    def init_ui(self):
        self.distance_label = ttk.Label(self, text="Distanța parcursă (km):")
        self.distance_edit = ttk.Entry(self)
        self.minutes_label = ttk.Label(self, text="Minute:")
        self.minutes_edit = ttk.Entry(self, validate="key", validatecommand=(self.register(self.validate_int), '%P'))
        self.seconds_label = ttk.Label(self, text="Secunde:")
        self.seconds_edit = ttk.Entry(self, validate="key", validatecommand=(self.register(self.validate_float), '%P'))
        self.result_label = ttk.Label(self, text="Viteza (km/h):")
        self.calculate_btn = ttk.Button(self, text="Calculează", command=self.calculate)
        
        layout = ttk.Frame(self)
        layout.pack(pady=10)
        self.distance_label.pack(in_=layout, pady=5)
        self.distance_edit.pack(in_=layout, pady=5)
        self.minutes_label.pack(in_=layout, pady=5)
        self.minutes_edit.pack(in_=layout, pady=5)
        self.seconds_label.pack(in_=layout, pady=5)
        self.seconds_edit.pack(in_=layout, pady=5)
        self.calculate_btn.pack(in_=layout, pady=5)
        self.result_label.pack(in_=layout, pady=5)

    def validate_int(self, value):
        if value.isdigit() and 0 <= int(value) <= 10000:
            return True
        return False

    def validate_float(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def calculate(self):
        try:
            distance = float(self.distance_edit.get())
            minutes = int(self.minutes_edit.get())
            seconds = float(self.seconds_edit.get())
            total_time_hours = (minutes + seconds/60) / 60
            if total_time_hours == 0:
                self.result_label.config(text="Timpul nu poate fi 0.")
                return
            speed = distance / total_time_hours
            self.result_label.config(text=f"Viteza (km/h): {speed:.2f}")
        except ValueError:
            self.result_label.config(text="Introduceți valori numerice valide.")

if __name__ == "__main__":
    app = RunnerSpeedCalculator()
    app.mainloop()