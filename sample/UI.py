"""
UI
This class is designed as the primary window for the frontend.
"""
import tkinter as tk
from tkinter import ttk
from ListFrame import ListFrame
from ItemFrame import ItemFrame

class UI():
    def __init__(self, entity):
        # UI Variables
        self.root = tk.Tk()
        WIDTH = 650
        HEIGHT = 350
        
        # Window Settings
        self.root.title("GLG")
        self.root.geometry(f"{WIDTH}x{HEIGHT}")
        self.root.protocol("WM_DELETE_WINDOW", lambda: self.close())
        tabNotebook = ttk.Notebook(self.root)
        tabNotebook.pack(fill="both", expand=True)
        tabNotebook.bind('<<NotebookTabChanged>>', lambda event: self.updateLists())

        # Frame Variables
        listFrame = ListFrame(self.root).getFrame()
        itemNames = [entity for entity in entity.getEntities()]
        print(itemNames)
        itemFrame = ItemFrame(self.root).getFrame()
        # itemContainerFrame = ItemContainerFrame(self.root).getFrame()
        # locationFrame = locationFrame(self.root).getFrame()
        
        # Add all frames
        tabNotebook.add(listFrame, text="List")
        tabNotebook.add(itemFrame, text="Items")
        # tabNotebook.add(itemContainerFrame, text="Recipes")
        # tabNotebook.add(locationFrame, text="Locations")
        
        # Main Loop
        self.root.mainloop()

    def close(self):
        self.root.destroy()