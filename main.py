# NOTE: Temporary one-file version of the code until I can figure out how to refactor it. 
import tkinter as tk
from tkinter import ttk

class Backend:
    # NOTE: I may be able to get away with an abstract class because of how similar the recipe and item functions are
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
        print(f"Closing!\nItems:{self.get_item_lists('name')}\nRecipes:{self.get_recipe_lists('name')}")
        with open(self.filename, "w", encoding="utf-8") as f:
            f.write("\n".join(self.items + self.recipes))

        root.destroy()
    
    # TODO: Make non-hardcoded locations for this function
    def get_item_lists(self, section=None):
        item_names = [entry[2:].split('|')[0] for entry in self.items]
        college_aisles = [entry.split('|')[1] for entry in self.items]
        grandparents_aisles = [entry.split('|')[2] for entry in self.items]
        jordan_aisles = [entry.split('|')[3] for entry in self.items]

        if section == None:
            return self.items
        elif section == "name":
            return item_names
        elif section == "college":
            return college_aisles
        elif section == "grandparents":
            return grandparents_aisles
        elif section == "jordan":
            return jordan_aisles
        
    def add_item(self, entry):
        self.items.append(entry)
        self.item_names = [entry[2:].split('|')[0] for entry in self.items]

    def edit_item(self, old_name, entry):
        self.items[self.item_names.index(old_name)] = entry
        self.item_names = [entry[2:].split('|')[0] for entry in self.items]

    def delete_item(self, name):
        self.items.remove(self.item_names.index(name))

    def get_recipe_lists(self, section=None):
        recipe_names = [entry[2:].split('|')[0] for entry in self.recipes]
        recipe_items = [entry.split('|')[1] for entry in self.recipes]

        if section == None:
            return self.recipes
        elif section == "name":
            return recipe_names
        elif section == "items":
            return recipe_items
        
    def add_recipe(self, entry):
        self.recipes.append(entry)
        self.recipe_names = [entry[2:].split('|')[0] for entry in self.recipes]

    def edit_recipe(self, old_name, entry):
        self.recipes[self.recipe_names.index(old_name)] = entry
        self.recipe_names = [entry[2:].split('|')[0] for entry in self.recipes]

    def delete_recipe(self, name):
        self.recipes.remove(self.recipe_names.index(name))

    def generate_list(self, user_list):
        final_list = []

        for i in range(len(user_list)):
            if user_list[i] == self.item_names:
                final_list.append(f"{self.items[i]}")

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
        tab_ntbk.bind('<<NotebookTabChanged>>', lambda event: self.update_lists(backend))

        list_frame = tk.Frame(tab_ntbk)
        item_frame = tk.Frame(tab_ntbk)
        recipe_frame = tk.Frame(tab_ntbk)

        tab_ntbk.add(list_frame, text="List")
        tab_ntbk.add(item_frame, text="Items")
        tab_ntbk.add(recipe_frame, text="Recipes")

        # List Frame layout
        list_frame.columnconfigure(0, weight=1)
        list_frame.columnconfigure(1, weight=1)
        list_frame.rowconfigure(0, weight=1)

        user_list = tk.Text(list_frame, width=25)
        user_list.grid(column=0, row=0, sticky="nsew", padx=5, pady=5)
        
        generate_list_btn = tk.Button(list_frame, text="Generate List", command=lambda: self.backend.generate_list(user_list.get("1.0", "end-1c").split('\n\n')))
        generate_list_btn.grid(column=1, row=0, sticky="nsew", padx=5, pady=5)

            # Item Frame
        for col in range(2):
            item_frame.columnconfigure(col, weight=1)
            for row in range(3):
                item_frame.rowconfigure(row, weight=1)
        
        self.item_lbox = tk.Listbox(item_frame, listvariable=self.backend.get_item_lists())
        self.item_lbox.grid(column=0, row=0, rowspan=3)
        add_item_btn = tk.Button(item_frame, text="Add Item", command=lambda: backend.add_item(""))
        add_item_btn.grid(column=1, row=0)
        edit_item_btn = tk.Button(item_frame, text="Edit Item", command=lambda: backend.edit_item(""))
        edit_item_btn.grid(column=1, row=1)
        delete_item_btn = tk.Button(item_frame, text="Delete Item", command=lambda: backend.delete_item(""))
        delete_item_btn.grid(column=1, row=2)

            # Recipe Frame
        for col in range(2):
            recipe_frame.columnconfigure(col, weight=1)
            for row in range(3):
                recipe_frame.rowconfigure(row, weight=1)

        self.recipe_lbox = tk.Listbox(recipe_frame, listvariable=self.backend.get_recipe_lists())
        self.recipe_lbox.grid(column=0, row=0, rowspan=3)
        add_recipe_btn = tk.Button(recipe_frame, text="Add Recipe", command=lambda: backend.add_recipe(""))
        add_recipe_btn.grid(column=1, row=0)
        edit_recipe_btn = tk.Button(recipe_frame, text="Edit Recipe", command=lambda: backend.edit_recipe(""))
        edit_recipe_btn.grid(column=1, row=1)
        delete_recipe_btn = tk.Button(recipe_frame, text="Delete Recipe", command=lambda: backend.delete_recipe(""))
        delete_recipe_btn.grid(column=1, row=2)

        root.mainloop()

    def update_lists(self, backend):
        # Item List
        self.item_lbox.delete(0, tk.END)
        for item in self.backend.get_item_lists("name"):
            self.item_lbox.insert(tk.END, item)

        # Recipe List
        self.recipe_lbox.delete(0, tk.END)
        for recipe in self.backend.get_recipe_lists("name"):
            self.recipe_lbox.insert(tk.END, recipe)

# Main Loop
def main():
    backend = Backend()
    print(backend.get_item_lists())
    
    frontend = Frontend(backend)

if __name__ == "__main__":
    main()