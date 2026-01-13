"""
UI
This class is designed as the primary window for the frontend.
"""
import tkinter as tk
from tkinter import ttk
from ListFrame import ListFrame
from ItemFrame import ItemFrame
from ItemContainerFrame import ItemContainerFrame
from LocationFrame import LocationFrame

class UI():
    def __init__(self, entityHandler, listGenerator, location):
        # UI Variables
        self.root = tk.Tk()
        WIDTH = 650
        HEIGHT = 350
        
        # Window Settings
        self.root.title("GLG")
        self.root.geometry(f"{WIDTH}x{HEIGHT}")
        self.root.protocol("WM_DELETE_WINDOW", lambda: self.close())
        tabNotebook = ttk.Notebook(self.root)
        tabNotebook.bind('<<NotebookTabChanged>>', lambda event: self.updateLists())
        tabNotebook.pack(fill="both", expand=True)

        # Object Variables
        self.listGeneratorObject = listGenerator
        self.entityHandlerObject = entityHandler
        self.locationObject = location
        # Frame Object Variables
        self.listFrameObject = ListFrame(self.root)
        itemNames = []
        # itemNames = [
        #     item.name for item in self.entityHandler.getEntities().values()
        #     if item.kind == "Item"]
        itemContainerNames = []
        locations = []
        self.itemFrameObject = ItemFrame(self.root, itemNames)
        self.itemContainerFrameObject = ItemContainerFrame(self.root, itemContainerNames)
        self.locationFrameObject = LocationFrame(self.root, locations)
        
        # Add all frames
        tabNotebook.add(self.listFrameObject, text="List")
        tabNotebook.add(self.itemFrameObject, text="Items")
        tabNotebook.add(self.itemContainerFrameObject, text="Recipes")
        tabNotebook.add(self.locationFrameObject, text="Locations")
        
        # Bind Virtual Events
        commands = [
            '<<generateList>>',
            '<<ListboxSelect>>',
            '<<addItem>>',
            '<<editItem>>',
            '<<removeItem>>',
            '<<addItemContainer>>',
            '<<editItemContainer>>',
            '<<removeItemContainer>>',
            '<<addLocation>>',
            '<<editLocation>>',
            '<<removeLocation>>'
            ]

        for command in commands:
            self.root.bind(command, lambda event, eventCommand=command: self.parseChoice(eventCommand))    
        
        self.root.mainloop()

    def close(self):
        self.root.quit()

    def parseChoice(self, choice):
        match choice:
            case "<<generateList>>":
                userListText = self.listFrameObject.getUserList()
                print(userListText)
                # self.listGenerator.generateList()
                # print(self.listGenerator.getList())
            case "<<getEntity>>":
                print(self.entityHandler.getEntity())
            case "<<addItem>>":
                print("Item added!")
            case "<<editItem>>":
                print("Item edited!")
            case "<<removeItem>>":
                print("Item removed!")
            case "<<addItemContainer>>":
                print("Recipe added!")
            case "<<editItemContainer>>":
                print("Recipe edited!")
            case "<<removeItemContainer>>":
                print("Recipe removed!")
            case "<<addLocation>>":
                print("Location added!")
            case "<<editLocation>>":
                print("Location edited!")
            case "<<removeLocation>>":
                print("Location removed!")

if __name__ == '__main__':
    UI.UI()