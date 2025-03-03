import tkinter as tk
from tkinter import ttk

class CircuitCurrentCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calcul Curent Circuit")
        self.init_ui()
        
    def init_ui(self):
        self.res1_label = ttk.Label(self, text="Rezistența R1 (ohmi):")
        self.res1_edit = ttk.Entry(self, validate="key", validatecommand=(self.register(self.validate_float), '%P'))
        
        self.res2_label = ttk.Label(self, text="Rezistența R2 (ohmi):")
        self.res2_edit = ttk.Entry(self, validate="key", validatecommand=(self.register(self.validate_float), '%P'))
        
        self.series_radio = ttk.Radiobutton(self, text="Serie", value="serie")
        self.parallel_radio = ttk.Radiobutton(self, text="Paralel", value="paralel")
        self.series_radio.invoke()
        
        self.calculate_btn = ttk.Button(self, text="Calculează", command=self.calculate)
        
        self.result_label = ttk.Label(self, text="Curentul circuitului (A):")
        
        self.res1_label.pack(pady=5)
        self.res1_edit.pack(pady=5)
        self.res2_label.pack(pady=5)
        self.res2_edit.pack(pady=5)
        self.series_radio.pack(pady=5)
        self.parallel_radio.pack(pady=5)
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
            R1 = float(self.res1_edit.get())
            R2 = float(self.res2_edit.get())
            if self.series_radio.instate(['selected']):
                R_total = R1 + R2
            else:
                if R1 == 0 or R2 == 0:
                    self.result_label.config(text="Rezistența nu poate fi 0 pentru conexiune paralelă.")
                    return
                R_total = 1 / (1 / R1 + 1 / R2)
            I = 220 / R_total if R_total != 0 else 0
            self.result_label.setText(f"Curentul circuitului: {I:.2f} A")
        except Exception:
            self.result_label.setText("Eroare: Verificați inputul.")

if __name__ == "__main__":
    app = CircuitCurrentCalculator()
    app.mainloop()