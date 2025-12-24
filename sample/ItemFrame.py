"""
ItemFrame
This class is designed as the Item configuration screen.
"""
import tkinter as tk

class ItemFrame(tk.Frame):
    def __init__(self, frame, itemNames=[]):
        super().__init__()

        columnCount = 3
        rowCount = 7

        for column in range(columnCount):
            self.columnconfigure(column, weight=1)
            
            for row in range(rowCount):
                self.rowconfigure(row, weight=1)

        # Item Listbox
        self.itemListbox = tk.Listbox(self, listvariable=itemNames)
        self.itemListbox.grid(column=0, row=0, rowspan=4)
        # Add Item Button
        self.addItemButton = tk.Button(self, text="Save New Item", command=lambda: self.event_generate("<<addItem>>"))
        self.addItemButton.grid(column=0, row=4, columnspan=3)
        # Edit Item Button
        self.editItemButton = tk.Button(self, text="Save Item", command=lambda: self.event_generate("<<editItem>>"))
        self.editItemButton.grid(column=0, row=5, columnspan=3)
        # Remove Item Button
        self.removeItemButton = tk.Button(self, text="Remove Item", command=lambda: self.event_generate("<<removeItem>>"))
        self.removeItemButton.grid(column=0, row=6, columnspan=3)