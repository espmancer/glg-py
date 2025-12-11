"""
ListFrame
This class is designed as the list generation screen.
It inherits the UI class.
"""
import UI

class ListFrame(UI):
    def __init__(self):
        self.listFrame = tk.Frame(UI.tabNotebook)