import tkinter as tk
from Controller import Controller
from Item import Item

class App(tk.Frame):
    def __init__(self, root):
        self.root = root
        self.root.title("GLG")
        self.root.minsize(200, 200)
        self.root.maxsize(500, 500)
        self.root.geometry("300x300+50+50")
        self.create_widgets()
        
    def create_widgets(self):
        # Options Grid 
        options_rows = 3
        options_columns = 3
        for columns in range(options_columns):
            self.root.columnconfigure(columns, weight = 1)

            for rows in range(options_rows):
                self.root.rowconfigure(rows, weight = 1)
                            
        # Items #
        # Item List
        item_listbox = tk.Listbox(root)
        
        for item in Controller.return_item_list():
            item_listbox.insert(tk.END, item)

        item_listbox.grid(column = 0, row = 0, rowspan = 3)

        # Add Item
        add_item_btn = tk.Button(root, text = "Add Item", command = lambda: Item.open_item_window(self))
        add_item_btn.grid(column = 1, row = 0, padx = 3)

        # Edit Item
        edit_item_btn = tk.Button(root, text = "Edit Item")
        edit_item_btn.grid(column = 1, row = 1, padx = 3)

        # Remove Item
        remove_item_btn = tk.Button(root, text = "Remove Item")
        remove_item_btn.grid(column = 1, row = 2, padx = 3)

        # Recipes #
        # Add Recipe
        add_recipe_btn = tk.Button(root, text = "Add Recipe")
        add_recipe_btn.grid(column = 2, row = 0)

        # Edit Recipe 
        edit_recipe_btn = tk.Button(root, text = "Edit Recipe")
        edit_recipe_btn.grid(column = 2, row = 1)

        # Remove Recipe
        remove_recipe_btn = tk.Button(root, text = "Remove Recipe")
        remove_recipe_btn.grid(column = 2, row = 2)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()