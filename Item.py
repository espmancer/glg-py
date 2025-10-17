import tkinter as tk

class Item:
    def __init__(self,root):
        self.root = root

    @staticmethod
    def open_item_window(self):
        item_window = tk.Toplevel(self.root)    
        item_window.title("Item")
        item_window.geometry("200x200+50+50")
        tk.Label(item_window, text = "Item Name").pack()
        tk.Entry(item_window).pack()