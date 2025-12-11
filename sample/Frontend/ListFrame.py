"""
ListFrame
This class is designed as the list generation screen.
"""
class ListFrame():
    def __init__(self, frame):
        self.listFrame = tk.Frame(frame)
        self.choice = ""

        listFrame.columnconfigure(0, weight=1)
        listFrame.columnconfigure(1, weight=1)
        listFrame.rowconfigure(0, weight=1)

        # User List (Text Widget)
        userList = tk.Text(listFrame, width=25)
        userList.grid(column=0, row=0, sticky="nsew", padx=5, pady=5)

        # Generate List Button
        generateListButton = tk.Button(listFrame, text="Generate List", command=lambda: setChoice("generateList"))
        generateListButton.grid(column=1, row=0, sticky="nsew", padx=5, pady=5)
    
    # Get the button choice
    def getChoice(self) -> str:
        return self.choice
    
    def setChoice(self, choice):
        self.choice = choice