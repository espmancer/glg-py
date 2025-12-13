"""
ItemFrame
This class is designed as the Item configuration screen.
"""
from tkinter import Frame, Listbox, Label, Entry, OptionMenu

class ItemFrame(Frame):
    def __init__(self, frame, itemNames=[]):
        self.itemFrame = Frame(frame)
        self.choice = ""
        columnCount = 3
        rowCount = 7

        for column in range(columnCount):
            self.itemFrame.columnconfigure(column, weight=1)
            
            for row in range(rowCount):
                self.itemFrame.rowconfigure(row, weight=1)

        # Item Listbox
        self.itemListbox = Listbox(self.itemFrame, listvariable=itemNames)
        self.itemListbox.bind('<<ListboxSelect>>', lambda: setChoice("selectItem"))
        self.itemListbox.grid(column=0, row=0, rowspan=4)

    # Get the choice of button.
    def getChoice(self) -> str:
        return self.choice
    
    # Get the listFrame.
    def getFrame(self) -> Frame:
        return self.itemFrame 

    # Set the choice of button.
    def setChoice(self, choice):
        self.choice = choice