"""
ListFrame
This class is designed as the list generation screen.
"""
from tkinter import Frame, Text, Button

class ListFrame(Frame):
    def __init__(self, frame):
        self.listFrame = Frame(frame)
        self.choice = ""

        self.listFrame.columnconfigure(0, weight=1)
        self.listFrame.columnconfigure(1, weight=1)
        self.listFrame.rowconfigure(0, weight=1)

        # User List (Text Widget)
        userList = Text(self.listFrame, width=25)
        userList.grid(column=0, row=0, sticky="nsew", padx=5, pady=5)

        # Generate List Button
        generateListButton = Button(self.listFrame, text="Generate List", command=lambda: setChoice("generateList"))
        generateListButton.grid(column=1, row=0, sticky="nsew", padx=5, pady=5)
    
    # Get the choice of button.
    def getChoice(self) -> str:
        return self.choice
    
    # Get the listFrame.
    def getFrame(self) -> Frame:
        return self.listFrame 

    # Set the choice of button.
    def setChoice(self, choice):
        self.choice = choice