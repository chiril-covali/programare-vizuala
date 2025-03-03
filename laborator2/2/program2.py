import tkinter as tk
from tkinter import ttk

class WindSpeedConverterInt(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Viteza vântului (număr întreg pozitiv)")
        self.init_ui()

    def init_ui(self):
        self.input_label = ttk.Label(self, text="Introduceți viteza (m/s):")
        self.input_edit = ttk.Entry(self, validate="key", validatecommand=(self.register(self.validate_int), '%P'))
        self.result_label = ttk.Label(self, text="Rezultat (km/h):")
        self.calculate_btn = ttk.Button(self, text="Calculează", command=self.calculate)

        self.input_label.pack(pady=5)
        self.input_edit.pack(pady=5)
        self.calculate_btn.pack(pady=5)
        self.result_label.pack(pady=5)

    def validate_int(self, value):
        if value.isdigit() and 0 <= int(value) <= 10000:
            return True
        return False

    def calculate(self):
        try:
            mps = int(self.input_edit.get())
            kmh = mps * 3.6
            self.result_label.config(text=f"Rezultat (km/h): {kmh:.2f}")
        except ValueError:
            self.result_label.config(text="Introduceți un număr întreg pozitiv.")

if __name__ == "__main__":
    app = WindSpeedConverterInt()
    app.mainloop()