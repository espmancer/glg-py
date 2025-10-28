import tkinter as tk
root = tk.Tk()

items = ['I:Item A|A2|A3|A4']
item_lbox = tk.Listbox(root, listvariable=items)
item_lbox.pack()

tk.mainloop()