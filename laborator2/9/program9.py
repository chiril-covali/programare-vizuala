import tkinter as tk
from tkinter import ttk, messagebox

class DiscountCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calcul Preț cu Reducere")
        self.init_ui()

    def init_ui(self):
        self.input_label = ttk.Label(self, text="Introduceți suma de cumpărare (ruble):")
        self.input_edit = ttk.Entry(self, validate="key", validatecommand=(self.register(self.validate_float), '%P'))
        self.calculate_btn = ttk.Button(self, text="Calculează", command=self.calculate)
        
        layout = ttk.Frame(self)
        layout.pack(pady=10)
        self.input_label.pack(in_=layout, pady=5)
        self.input_edit.pack(in_=layout, pady=5)
        self.calculate_btn.pack(in_=layout, pady=5)
    
    def validate_float(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def calculate(self):
        try:
            amount = float(self.input_edit.get())
            discount_pct = 0
            if amount > 1000:
                discount_pct = 3
            elif amount > 500:
                discount_pct = 2
            elif amount > 300:
                discount_pct = 1
            
            discount_value = amount * discount_pct / 100
            final_price = amount - discount_value
            
            messagebox.showinfo("Reducere", f"Reducere: {discount_pct}%\nValoare reducere: {discount_value:.2f} ruble\nPreț final: {final_price:.2f} ruble")
        except ValueError:
            pass

if __name__ == "__main__":
    app = DiscountCalculator()
    app.mainloop()
