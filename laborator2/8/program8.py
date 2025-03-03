import tkinter as tk
from tkinter import ttk

class ParallelCurrentCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calcul Curent în Circuit Paralel")
        self.init_ui()

    def init_ui(self):
        self.res1_label = ttk.Label(self, text="Rezistența R1 (ohmi):")
        self.res1_edit = ttk.Entry(self, validate="key", validatecommand=(self.register(self.validate_float), '%P'))
        
        self.res2_label = ttk.Label(self, text="Rezistența R2 (ohmi):")
        self.res2_edit = ttk.Entry(self, validate="key", validatecommand=(self.register(self.validate_float), '%P'))
        
        self.calculate_btn = ttk.Button(self, text="Calculare", command=self.calculate)
        self.result_label = ttk.Label(self, text="Curentul (A):")
        
        layout = ttk.Frame(self)
        layout.pack(pady=10)
        self.res1_label.pack(in_=layout, pady=5)
        self.res1_edit.pack(in_=layout, pady=5)
        self.res2_label.pack(in_=layout, pady=5)
        self.res2_edit.pack(in_=layout, pady=5)
        self.calculate_btn.pack(in_=layout, pady=5)
        self.result_label.pack(in_=layout, pady=5)
    
    def validate_float(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False
    
    def calculate(self):
        try:
            R1 = float(self.res1_edit.get())
            R2 = float(self.res2_edit.get())
            if R1 <= 0 or R2 <= 0:
                self.result_label.config(text="Rezistențele trebuie să fie > 0.")
                return
            # Rezistență echivalentă pentru două rezistențe în paralel:
            R_eq = 1 / (1/R1 + 1/R2)
            I = 220 / R_eq
            self.result_label.config(text=f"Curentul (A): {I:.2f}")
        except ValueError:
            self.result_label.config(text="Introduceți valori numerice valide.")

if __name__ == "__main__":
    app = ParallelCurrentCalculator()
    app.mainloop()