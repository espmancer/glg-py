import tkinter as tk

class App(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        
        add_item_btn = tk.Button(root, text = "Add Item", command = "add_item")

# root.title("GLG")
# root.minsize(200, 200)
# root.maxsize(500, 500)
# root.geometry("300x300+50+50")

if __name__ == "__main__":
    root = tk.Tk()
    App(root).pack(side="top", fill="both", expand=True)
    root.mainloop()