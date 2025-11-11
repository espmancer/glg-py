import tkinter as tk
root = tk.Tk()

listbox = tk.Listbox(root)

listbox.insert(1, "A")

listbox.get(int(listbox.curselection()))

root.mainloop()