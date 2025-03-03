import tkinter as tk
from tkinter import ttk

class DepositCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator Randament Depozit")
        self.init_ui()
        
    def init_ui(self):
        self.amount_label = ttk.Label(self, text="Suma Depozit (lei):")
        self.amount_edit = ttk.Entry(self, validate="key", validatecommand=(self.register(self.validate_float), '%P'))
        
        self.years_label = ttk.Label(self, text="Număr de ani:")
        self.years_edit = ttk.Entry(self, validate="key", validatecommand=(self.register(self.validate_int), '%P'))
        
        self.rate_label = ttk.Label(self, text="Rata dobânzii (% anual):")
        self.rate_edit = ttk.Entry(self, validate="key", validatecommand=(self.register(self.validate_float), '%P'))
        
        self.simple_radio = ttk.Radiobutton(self, text="Dobândă Simplă", value="simple")
        self.compound_radio = ttk.Radiobutton(self, text="Dobândă Compusă", value="compound")
        self.simple_radio.invoke()
        
        self.calculate_btn = ttk.Button(self, text="Calculează", command=self.calculate)
        
        self.result_label = ttk.Label(self, text="Randament:")
        
        self.amount_label.pack(pady=5)
        self.amount_edit.pack(pady=5)
        self.years_label.pack(pady=5)
        self.years_edit.pack(pady=5)
        self.rate_label.pack(pady=5)
        self.rate_edit.pack(pady=5)
        self.simple_radio.pack(pady=5)
        self.compound_radio.pack(pady=5)
        self.calculate_btn.pack(pady=5)
        self.result_label.pack(pady=5)
        
    def validate_float(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False
        
    def validate_int(self, value):
        try:
            int(value)
            return True
        except ValueError:
            return False
        
    def calculate(self):
        try:
            P = float(self.amount_edit.get())
            t = int(self.years_edit.get())
            r = float(self.rate_edit.get()) / 100.0
            if self.simple_radio.instate(['selected']):
                # Dobânda simplă: A = P * (1 + r * t)
                A = P * (1 + r * t)
                interest_type = "Simplă"
            else:
                # Dobânda compusă (compunere lunară):
                n = 12
                A = P * (1 + r/n) ** (n * t)
                interest_type = "Compusă"
            self.result_label.config(text=f"Randament ({interest_type}): {A:.2f} lei")
        except Exception:
            self.result_label.config(text="Eroare: Verificați datele introduse.")

if __name__ == "__main__":
    app = DepositCalculator()
    app.mainloop()
