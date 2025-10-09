import tkinter as tk

class App:
    def __init__(root):
        root.title("GLG")
        root.minsize(200, 200)
        root.maxsize(500, 500)
        root.geometry("300x300+50+50")
    def launch(root):
        root.mainloop()

App.launch(tk.Tk())


