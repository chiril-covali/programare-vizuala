import tkinter as tk
from tkinter import ttk, messagebox

class TripCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator Cost Călătorie")
        self.init_ui()
        
    def init_ui(self):
        self.distance_label = ttk.Label(self, text="Distanța (km):")
        self.distance_input = ttk.Entry(self)
        
        self.fuel_label = ttk.Label(self, text="Consum (l/100km):")
        self.fuel_input = ttk.Entry(self)
        
        self.price_label = ttk.Label(self, text="Preț combustibil (MDL/l):")
        self.price_input = ttk.Entry(self)
        
        self.result_label = ttk.Label(self, text="Cost total:")
        
        self.calc_button = ttk.Button(self, text="Calculează", command=self.calculate_cost)
        
        layout = ttk.Frame(self)
        layout.pack(pady=10)
        self.distance_label.pack(in_=layout, pady=5)
        self.distance_input.pack(in_=layout, pady=5)
        self.fuel_label.pack(in_=layout, pady=5)
        self.fuel_input.pack(in_=layout, pady=5)
        self.price_label.pack(in_=layout, pady=5)
        self.price_input.pack(in_=layout, pady=5)
        self.calc_button.pack(in_=layout, pady=5)
        self.result_label.pack(in_=layout, pady=5)
        
    def calculate_cost(self):
        try:
            distance = float(self.distance_input.get())
            consumption = float(self.fuel_input.get())
            price = float(self.price_input.get())
            
            cost = distance * (consumption / 100) * price
            self.result_label.config(text=f"Cost total: {cost:.2f} MDL")
        except ValueError:
            messagebox.showwarning("Eroare", "Introduceți valori numerice valide.")

if __name__ == '__main__':
    app = TripCalculator()
    app.mainloop()
