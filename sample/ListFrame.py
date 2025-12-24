"""
ListFrame
This class is designed as the list generation screen.
"""
from tkinter as tk

class ListFrame(Frame):
    def __init__(self, root):
        super().__init__()

        # User List (Text Widget)
        self.userList = Text(root, width=25)
        self.userList.grid(column=0, row=0, sticky="nsew", padx=5, pady=5)
        # Generate List Button
        self.generateListButton = Button(root, text="Generate List", command=lambda: self.event_generate("<<generateList>>"))
        self.generateListButton.grid(column=1, row=0, sticky="nsew", padx=5, pady=5)

    # Get the user list.
    def getUserList(self) -> str:
        return self.userList.get("1.0", "end")