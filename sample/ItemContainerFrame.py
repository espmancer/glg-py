"""
ItemContainerFrame
This class is designed as the ItemContainer (recipe) configuration screen.
"""
import tkinter as tk

class ItemFrame(tk.Frame):
    def __init__(self, frame, itemContainerNames=[]):
        super().__init__()

        columnCount = 2
        rowCount = 7

        for column in range(columnCount):
            self.columnconfigure(column, weight=1)
            
            for row in range(rowCount):
                self.rowconfigure(row, weight=1)

        # Item Listbox
        self.itemContainerListbox = tk.Listbox(self, listvariable=itemContainerNames)
        self.itemContainerListbox.grid(column=0, row=0, rowspan=4)
        # Add Item Button
        self.addItemContainerButton = tk.Button(self, text="Save New Recipe", command=lambda: self.event_generate("<<addItemContainer>>"))
        self.addItemContainerButton.grid(column=0, row=4, columnspan=3)
        # Edit Item Button
        self.editItemContainerButton = tk.Button(self, text="Save Recipe", command=lambda: self.event_generate("<<editItemContainer>>"))
        self.editItemContainerButton.grid(column=0, row=5, columnspan=3)
        # Remove Item Button
        self.removeItemContainerButton = tk.Button(self, text="Remove Recipe", command=lambda: self.event_generate("<<removeItemContainer>>"))
        self.removeItemContainerButton.grid(column=0, row=6, columnspan=3)