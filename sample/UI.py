"""
UI
This class is designed as the primary window for the frontend.
"""
from tkinter import tk, ttk

class UI():
    WIDTH = 650
    HEIGHT = 350

    def __init__(self, root=tk.Tk()):
        self.root = root

        root.title("GLG")
        root.geometry(f"{WIDTH}x{HEIGHT}")
        root.protocol("WM_DELETE_WINDOW", lambda: self.close())
        tabNotebook = ttk.Notebook(self.root)
        tabNotebook.pack(fill="both", expand=True)
        tabNotebook.bind('<<NotebookTabChanged>>', lambda event: self.updateLists())