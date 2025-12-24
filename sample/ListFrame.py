"""
ListFrame
This class is designed as the list generation screen.
"""
import tkinter as tk

class ListFrame(tk.Frame):
    def __init__(self, root):
        super().__init__()

        # Set Up Grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        # User List (Text Widget)
        self.userList = tk.Text(self, width=25)
        self.userList.grid(column=0, row=0, sticky="nsew", padx=5, pady=5)
        # Generate List Button
        self.generateListButton = tk.Button(self, text="Generate List", command=lambda: self.event_generate("<<generateList>>"))
        self.generateListButton.grid(column=1, row=0, sticky="nsew", padx=5, pady=5)

    # Get the user list.
    def getUserList(self) -> str:
        return self.userList.get("1.0", "end")