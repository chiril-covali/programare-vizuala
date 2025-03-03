import tkinter as tk
from tkinter import ttk

class WindSpeedConverter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Viteza vântului - m/s la km/h")
        self.init_ui()
    
    def init_ui(self):
        self.input_label = ttk.Label(self, text="Introduceți viteza (m/s):")
        self.input_edit = ttk.Entry(self)
        self.result_label = ttk.Label(self, text="Rezultat (km/h):")
        self.calculate_btn = ttk.Button(self, text="Calculează", command=self.calculate)
        
        self.input_label.pack(pady=5)
        self.input_edit.pack(pady=5)
        self.calculate_btn.pack(pady=5)
        self.result_label.pack(pady=5)
    
    def calculate(self):
        try:
            mps = float(self.input_edit.get())
            kmh = mps * 3.6
            self.result_label.config(text=f"Rezultat (km/h): {kmh:.2f}")
        except ValueError:
            self.result_label.config(text="Introduceți o valoare numerică validă.")

if __name__ == "__main__":
    app = WindSpeedConverter()
    app.mainloop()