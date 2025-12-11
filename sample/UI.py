"""
UI
This class is designed as the primary window for the frontend.
"""
import tkinter as tk
from tkinter import ttk
from ListFrame import ListFrame

class UI():
    def __init__(self, entity):
        # UI Variables
        self.entity = entity
        root = tk.Tk()
        WIDTH = 650
        HEIGHT = 350
        
        # Window Settings
        root.title("GLG")
        root.geometry(f"{WIDTH}x{HEIGHT}")
        root.protocol("WM_DELETE_WINDOW", lambda: self.close())
        tabNotebook = ttk.Notebook(root)
        tabNotebook.pack(fill="both", expand=True)
        tabNotebook.bind('<<NotebookTabChanged>>', lambda event: self.updateLists())

        # Frame Variables
        listFrame = ListFrame(root).getListFrame()
        
        # Add all frames
        tabNotebook.add(listFrame, text="List")
        root.mainloop()
    
    