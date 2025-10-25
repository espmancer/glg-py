# NOTE: Temporary one-file version of the code until I can figure out how to refactor it. 
import tkinter as tk
from tkinter import ttk

class Backend:
    def __init__(self, filename="grocery_list.txt"):
        self.filename = filename

        try:
            with open(self.filename, "x", encoding="utf-8") as f:   
                self.raw_list = ""
        except FileExistsError:
            with open(self.filename, "r", encoding="utf-8") as f:   
                self.raw_list = f.read().splitlines()
        self.items = [entry for entry in self.raw_list if entry.startswith("I:")]
        self.item_names = [entry[2:].split('|')[0] for entry in self.items if entry[0] == 'I']
        self.recipes = [entry for entry in self.raw_list if entry.startswith("R:")]
        self.recipe_names = [entry[2:].split('|')[0] for entry in self.items if entry[0] == 'R']
        self.locations = ["College", "Grandparents", "Jordan"]
           
    def close(self, root):
        print(f"Closing!\nItems:{','.join(self.item_names)}\nRecipes:{self.recipes}")
        with open(self.filename, "w", encoding="utf-8") as f:
            f.write("\n".join(self.items + self.recipes))

        root.destroy()
    
    def get_item_list(self):
        return self.items

    def add_item(self, entry):
        self.items.append(entry)
        self.item_names = [entry[2:].split('|')[0] for entry in self.items if entry[0] == 'I']

    def add_recipe(self, entry):
        self.recipes.append(entry)

    def edit_item(self, old_name, entry):
        self.items[self.item_names.index(old_name)] = entry
        self.item_names = [entry[2:].split('|')[0] for entry in self.items if entry[0] == 'I']

class Frontend:
    def __init__(self, backend, root=tk.Tk()):
        self.backend = backend
        self.root = root

        root.title("GLG")
        root.minsize(200, 200)
        root.maxsize(500, 500)
        root.geometry("300x300+50+50")
        root.protocol("WM_DELETE_WINDOW", lambda: self.backend.close(root))

        # Main Menu (Notebook)
        tab_ntbk = ttk.Notebook(root)
        tab_ntbk.pack(fill="both", expand=True)

        list_frame = tk.Frame(tab_ntbk)
        item_frame = tk.Frame(tab_ntbk)
        recipe_frame = tk.Frame(tab_ntbk)

        tab_ntbk.add(list_frame, text="List")
        tab_ntbk.add(item_frame, text="Items")
        tab_ntbk.add(recipe_frame, text="Recipes")

        # List Frame layout
        list_frame.columnconfigure(0, weight=3)
        list_frame.columnconfigure(1, weight=1)
        list_frame.rowconfigure(0, weight=1)

        user_list = tk.Text(list_frame, width=25)
        user_list.grid(column=0, row=0, sticky="nsew", padx=5, pady=5)

        generate_list_btn = tk.Button(list_frame, text="Generate List")
        generate_list_btn.grid(column=1, row=0, sticky="nsew", padx=5, pady=5)

        root.mainloop()

# Main Loop
def main():
    backend = Backend()
    backend.add_item("I:Item A|A1|A2|A3")
    backend.edit_item("Item A", "I:Item B|A2|A3|A4")
    print(backend.get_item_list())
    
    frontend = Frontend(backend)

if __name__ == "__main__":
    main()