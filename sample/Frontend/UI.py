"""
UI
This class is designed as the primary window for the frontend.
"""
import tkinter as tk
from tkinter import ttk

class UI():
    def __init__(self, entity, root=tk.Tk()):
        self.root = root
        self.entity = entity
        WIDTH = 650
        HEIGHT = 350
        
        root.title("GLG")
        root.geometry(f"{WIDTH}x{HEIGHT}")
        root.protocol("WM_DELETE_WINDOW", lambda: self.close())
        tabNotebook = ttk.Notebook(self.root)
        tabNotebook.pack(fill="both", expand=True)
        tabNotebook.bind('<<NotebookTabChanged>>', lambda event: self.updateLists())

        ListFrame()

        self.root.mainloop()