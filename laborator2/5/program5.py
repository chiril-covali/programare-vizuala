import tkinter as tk
from tkinter import ttk

class PoundToKgPositive(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Livre în Kilograme - Număr pozitiv")
        self.init_ui()

    def init_ui(self):
        self.input_label = ttk.Label(self, text="Introduceți masa (lire):")
        self.input_edit = ttk.Entry(self, validate="key", validatecommand=(self.register(self.validate_float), '%P'))
        self.result_label = ttk.Label(self, text="Masa în kilograme:")
        self.calculate_btn = ttk.Button(self, text="Calculează", command=self.calculate)

        self.input_label.pack(pady=5)
        self.input_edit.pack(pady=5)
        self.calculate_btn.pack(pady=5)
        self.result_label.pack(pady=5)

    def validate_float(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def calculate(self):
        try:
            lb = float(self.input_edit.get())
            kg = lb * 0.4095
            self.result_label.config(text=f"Masa în kilograme: {kg:.3f}")
        except ValueError:
            self.result_label.config(text="Introduceți o valoare numerică pozitivă.")

if __name__ == "__main__":
    app = PoundToKgPositive()
    app.mainloop()