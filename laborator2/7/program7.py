import tkinter as tk
from tkinter import ttk

class CurrentCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calcul Curent (V=220V)")
        self.init_ui()

    def init_ui(self):
        self.res_label = ttk.Label(self, text="Introduceți rezistența (ohmi):")
        self.res_edit = ttk.Entry(self, validate="key", validatecommand=(self.register(self.validate_float), '%P'))
        self.res_edit.bind("<KeyRelease>", self.enable_button)
        self.calculate_btn = ttk.Button(self, text="Calculare", command=self.calculate)
        self.calculate_btn.config(state='disabled')
        self.result_label = ttk.Label(self, text="Curentul (A):")
        
        layout = ttk.Frame(self)
        layout.pack(pady=10)
        self.res_label.pack(in_=layout, pady=5)
        self.res_edit.pack(in_=layout, pady=5)
        self.calculate_btn.pack(in_=layout, pady=5)
        self.result_label.pack(in_=layout, pady=5)
        
    def validate_float(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False
    
    def enable_button(self, event):
        self.calculate_btn.config(state='normal' if self.res_edit.get().strip() else 'disabled')
    
    def calculate(self):
        try:
            R = float(self.res_edit.get())
            if R == 0:
                self.result_label.config(text="Rezistența nu poate fi 0.")
                return
            I = 220 / R
            self.result_label.config(text=f"Curentul (A): {I:.2f}")
        except ValueError:
            self.result_label.config(text="Introduceți o valoare numerică.")
            
if __name__ == "__main__":
    app = CurrentCalculator()
    app.mainloop()