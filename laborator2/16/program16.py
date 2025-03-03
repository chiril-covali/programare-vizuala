import tkinter as tk
from tkinter import ttk, messagebox

class SimpleCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator Adunare și Scădere")
        self.init_ui()
        
    def init_ui(self):
        # Display pentru introducerea expresiei și afișarea rezultatului
        self.display = ttk.Entry(self)
        self.display.config(state='readonly')
        
        # Creare butoane numerice 0-9 și conectarea unui handler comun
        self.buttons = {}
        for digit in range(10):
            self.buttons[str(digit)] = ttk.Button(self, text=str(digit), command=lambda d=str(digit): self.on_number_click(d))
            
        # Creare butoane pentru operatori și alte acțiuni
        self.add_button = ttk.Button(self, text="+", command=lambda: self.on_operator_click("+"))
        self.sub_button = ttk.Button(self, text="-", command=lambda: self.on_operator_click("-"))
        self.eq_button = ttk.Button(self, text="=", command=self.on_equals)
        self.clear_button = ttk.Button(self, text="Clear", command=self.on_clear)
        
        # Layout pentru butoanele numerice (dispunere în grilă)
        grid = ttk.Frame(self)
        # Dispunerea butoanelor: 7,8,9; 4,5,6; 1,2,3; 0
        positions = [(i, j) for i in range(4) for j in range(3)]
        num_order = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0']
        pos_map = {}
        index = 0
        for position in positions:
            if index < len(num_order):
                pos_map[num_order[index]] = position
                index += 1
                
        for num, pos in pos_map.items():
            grid.grid(row=pos[0], column=pos[1])
            self.buttons[num].grid(row=pos[0], column=pos[1])
        
        # Layout vertical pentru operatori
        operator_layout = ttk.Frame(self)
        self.add_button.pack(in_=operator_layout, pady=5)
        self.sub_button.pack(in_=operator_layout, pady=5)
        self.eq_button.pack(in_=operator_layout, pady=5)
        self.clear_button.pack(in_=operator_layout, pady=5)
        
        # Layout principal
        main_layout = ttk.Frame(self)
        self.display.pack(in_=main_layout, pady=5)
        grid.pack(in_=main_layout, pady=5)
        operator_layout.pack(in_=main_layout, pady=5)
        
        main_layout.pack(pady=10)
        
    def on_number_click(self, num):
        current_text = self.display.get()
        self.display.config(state='normal')
        self.display.insert(tk.END, num)
        self.display.config(state='readonly')
        
    def on_operator_click(self, op):
        current_text = self.display.get()
        # Evităm operatorii consecutivi
        if current_text and current_text[-1] not in "+-":
            self.display.config(state='normal')
            self.display.insert(tk.END, op)
            self.display.config(state='readonly')
        elif current_text:
            # Înlocuim ultimul operator dacă se apasă un nou operator
            self.display.config(state='normal')
            self.display.delete(len(current_text)-1, tk.END)
            self.display.insert(tk.END, op)
            self.display.config(state='readonly')
            
    def on_equals(self):
        expression = self.display.get()
        try:
            # Evaluăm expresia care conține numai cifre și operatori +, -
            result = eval(expression)
            self.display.config(state='normal')
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
            self.display.config(state='readonly')
        except Exception:
            messagebox.showwarning("Eroare", "Expresie invalidă.")
            
    def on_clear(self):
        self.display.config(state='normal')
        self.display.delete(0, tk.END)
        self.display.config(state='readonly')

if __name__ == '__main__':
    app = SimpleCalculator()
    app.mainloop()