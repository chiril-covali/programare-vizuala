import tkinter as tk
from tkinter import ttk, messagebox

class PurchaseCostCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Costul de Achiziție")
        # Dicționarul de produse: cod produs => {"nume": numeProdus, "pret": pretProdus}
        self.products = {
            "101": {"name": "Măr", "price": 2.50},
            "102": {"name": "Păr", "price": 3.00},
            "103": {"name": "Banane", "price": 1.80},
            "104": {"name": "Portocale", "price": 2.20},
        }
        self.init_ui()

    def init_ui(self):
        self.code_label = ttk.Label(self, text="Introduceți codul produsului:")
        self.code_edit = ttk.Entry(self)
        self.quantity_label = ttk.Label(self, text="Introduceți numărul de unități:")
        self.quantity_edit = ttk.Entry(self)
        self.quantity_edit.config(validate="key", validatecommand=(self.register(self.validate_quantity), '%P'))
        self.calculate_btn = ttk.Button(self, text="Calculează costul", command=self.calculate)
        self.result_label = ttk.Label(self, text="Costul total:")

        self.code_label.pack(pady=5)
        self.code_edit.pack(pady=5)
        self.quantity_label.pack(pady=5)
        self.quantity_edit.pack(pady=5)
        self.calculate_btn.pack(pady=5)
        self.result_label.pack(pady=5)
    
    def validate_quantity(self, value):
        if value.isdigit() and 1 <= int(value) <= 10000:
            return True
        return False

    def calculate(self):
        code = self.code_edit.get().strip()
        if code not in self.products:
            messagebox.showwarning("Eroare", "Produsul cu codul introdus nu există!")
            return
        try:
            quantity = int(self.quantity_edit.get())
        except ValueError:
            self.result_label.config(text="Introduceți o cantitate validă.")
            return
        product = self.products[code]
        total = product["price"] * quantity
        self.result_label.config(text=f"{product['name']} x {quantity} = {total:.2f} ruble")

if __name__ == "__main__":
    app = PurchaseCostCalculator()
    app.mainloop()