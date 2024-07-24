import tkinter as tk
from tkinter import messagebox
import sqlite3

# Database setup
conn = sqlite3.connect('sales.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS sales
             (id INTEGER PRIMARY KEY, product_name TEXT, price REAL, quantity INTEGER)''')
conn.commit()

# GUI setup
class SalesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sales Shop")
        
        # Product Name
        self.product_name_label = tk.Label(root, text="Product Name")
        self.product_name_label.grid(row=0, column=0)
        self.product_name_entry = tk.Entry(root)
        self.product_name_entry.grid(row=0, column=1)
        
        # Price
        self.price_label = tk.Label(root, text="Price")
        self.price_label.grid(row=1, column=0)
        self.price_entry = tk.Entry(root)
        self.price_entry.grid(row=1, column=1)
        
        # Quantity
        self.quantity_label = tk.Label(root, text="Quantity")
        self.quantity_label.grid(row=2, column=0)
        self.quantity_entry = tk.Entry(root)
        self.quantity_entry.grid(row=2, column=1)
        
        # Buttons
        self.add_button = tk.Button(root, text="Add Sale", command=self.add_sale)
        self.add_button.grid(row=3, column=0, columnspan=2)
        
        self.view_button = tk.Button(root, text="View Sales", command=self.view_sales)
        self.view_button.grid(row=4, column=0, columnspan=2)
    
    def add_sale(self):
        product_name = self.product_name_entry.get()
        price = float(self.price_entry.get())
        quantity = int(self.quantity_entry.get())
        
        c.execute("INSERT INTO sales (product_name, price, quantity) VALUES (?, ?, ?)",
                  (product_name, price, quantity))
        conn.commit()
        
        messagebox.showinfo("Success", "Sale added successfully")
    
    def view_sales(self):
        c.execute("SELECT * FROM sales")
        records = c.fetchall()
        
        view_window = tk.Toplevel(self.root)
        view_window.title("View Sales")
        
        for i, record in enumerate(records):
            for j, value in enumerate(record):
                label = tk.Label(view_window, text=value)
                label.grid(row=i, column=j)

root = tk.Tk()
app = SalesApp(root)
root.mainloop()

conn.close()
