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
        self.recipes = [entry for entry in self.raw_list if entry.startswith("R:")]
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

    def delete_item(self, name):
        self.items.pop(self.get_item_lists("name").index(name))

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

    def delete_recipe(self, name):
        self.recipes.pop(self.get_recipe_lists("name").index(name))

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
        tab_ntbk.bind('<<NotebookTabChanged>>', lambda event: self.update_lists())
        
        # Frames
        list_frame = tk.Frame(tab_ntbk)
        item_frame = tk.Frame(tab_ntbk)
        recipe_frame = tk.Frame(tab_ntbk)

            # Add Frames
        tab_ntbk.add(list_frame, text="List")
        tab_ntbk.add(item_frame, text="Items")
        tab_ntbk.add(recipe_frame, text="Recipes")

        # List Frame layout
        list_frame.columnconfigure(0, weight=1)
        list_frame.columnconfigure(1, weight=1)
        list_frame.rowconfigure(0, weight=1)

            # User List (Text Widget)
        user_list = tk.Text(list_frame, width=25)
        user_list.grid(column=0, row=0, sticky="nsew", padx=5, pady=5)

            # Generate List Button
        generate_list_btn = tk.Button(list_frame, text="Generate List", command=lambda: self.backend.generate_list(user_list.get("1.0", "end-1c").split('\n\n')))
        generate_list_btn.grid(column=1, row=0, sticky="nsew", padx=5, pady=5)

            # Item Frame
        for col in range(2):
            item_frame.columnconfigure(col, weight=1)
            for row in range(5):
                item_frame.rowconfigure(row, weight=1)
        
                # Item Listbox
        self.item_lbox = tk.Listbox(item_frame, listvariable=self.backend.get_item_lists())
        self.item_lbox.grid(column=0, row=0, rowspan=2)
        self.item_lbox.bind('<<ListboxSelect>>', self.select_item)
        
                # Item Name
        item_name_lbl = tk.Label(item_frame, text="Item Name:")
        item_name_lbl.grid(column=0, row=2)
        self.item_name_etr = tk.Entry(item_frame)
        self.item_name_etr.grid(column=1, row=2)
        
                # College Aisle
        college_aisle_lbl = tk.Label(item_frame, text="College Aisle:")
        college_aisle_lbl.grid(column=0, row=3)
        self.college_aisle_etr = tk.Entry(item_frame)
        self.college_aisle_etr.grid(column=1, row=3)
        
                # Grandparents Aisle
        grandparents_aisle_lbl = tk.Label(item_frame, text="Grandparents Aisle:")
        grandparents_aisle_lbl.grid(column=0, row=4)    
        self.grandparents_aisle_etr = tk.Entry(item_frame)
        self.grandparents_aisle_etr.grid(column=1, row=4)
        
                # Jordan Aisle
        jordan_aisle_lbl = tk.Label(item_frame, text="Jordan Aisle:")
        jordan_aisle_lbl.grid(column=0, row=5)
        self.jordan_aisle_etr = tk.Entry(item_frame)
        self.jordan_aisle_etr.grid(column=1, row=5)
        
                # Add Item Button
        add_item_btn = tk.Button(item_frame, text="Add Item", command=lambda: (
            self.backend.add_item(
                f"I:{self.item_name_etr.get()}|{self.college_aisle_etr.get()}|{self.grandparents_aisle_etr.get()}|{self.jordan_aisle_etr.get()}"
            ),
            self.update_lists()))
        add_item_btn.grid(column=1, row=0)
        
                # Delete Item Button
        delete_item_btn = tk.Button(item_frame, text="Delete Item", command=lambda: (self.backend.delete_item(self.item_name_etr.get()), self.update_lists()))
        delete_item_btn.grid(column=1, row=1)

            # Recipe Frame
        for col in range(2):
            recipe_frame.columnconfigure(col, weight=1)
            for row in range(3):
                recipe_frame.rowconfigure(row, weight=0)

        recipe_frame.rowconfigure(3, weight=3)
                # Recipe Listbox
        self.recipe_lbox = tk.Listbox(recipe_frame, listvariable=self.backend.get_recipe_lists())
        self.recipe_lbox.grid(column=0, row=0, rowspan=2)
        self.recipe_lbox.bind('<<ListboxSelect>>', self.select_recipe)


                # Recipe Name Entry
        recipe_name_lbl = tk.Label(recipe_frame, text="Recipe Name")
        recipe_name_lbl.grid(column=0, row=2)
        self.recipe_name_etr = tk.Entry(recipe_frame)
        self.recipe_name_etr.grid(column=1, row=2)

                # Recipe Items List (Text Widget)
        recipe_items_lbl = tk.Label(recipe_frame, text="Recipe Items")
        recipe_items_lbl.grid(column=0, row=3)
        self.recipe_items_list = tk.Text(recipe_frame, height=5, width=10)
        self.recipe_items_list.grid(column=1, row=3)

                # Add Recipe Button
        newline = '\n'
        add_recipe_btn = tk.Button(recipe_frame, text="Add Recipe", command=lambda: (self.backend.add_recipe(
            f"R:{self.recipe_name_etr.get()}|{self.recipe_items_list.get('1.0', 'end-1c').replace(newline, ',')}"
            ), self.update_lists()))
        add_recipe_btn.grid(column=1, row=0)
        
                # Delete Recipe Button
        delete_recipe_btn = tk.Button(recipe_frame, text="Delete Recipe", command=lambda: (self.backend.delete_recipe(self.recipe_name_etr.get()), self.update_lists()))
        delete_recipe_btn.grid(column=1, row=1)

        root.mainloop()

    def update_lists(self):
        # Item List
        self.item_lbox.delete(0, tk.END)
        for item in self.backend.get_item_lists("name"):
            self.item_lbox.insert(tk.END, item)

        # Recipe List
        self.recipe_lbox.delete(0, tk.END)
        for recipe in self.backend.get_recipe_lists("name"):
            self.recipe_lbox.insert(tk.END, recipe)

    def select_item(self, event):
        index = int(self.item_lbox.curselection()[0])
        self.set_text(self.item_name_etr, self.backend.get_item_lists("name")[index])
        self.set_text(self.college_aisle_etr, self.backend.get_item_lists("college")[index])
        self.set_text(self.grandparents_aisle_etr, self.backend.get_item_lists("grandparents")[index])
        self.set_text(self.jordan_aisle_etr, self.backend.get_item_lists("jordan")[index])

    def select_recipe(self, event):
        index = int(self.recipe_lbox.curselection()[0])
        self.set_text(self.recipe_name_etr, self.backend.get_recipe_lists("name")[index])
        newline_list = self.backend.get_recipe_lists("items")[index].replace(',','\n')
        self.set_text(self.recipe_items_list, newline_list)

    def set_text(self, entry, text):
        index = "1.0" if isinstance(entry, tk.Text) else 0 
        entry.delete(index, tk.END)
        entry.insert(index, text)
        
# Main Loop
def main():
    backend = Backend()
    print(backend.get_item_lists())
    
    frontend = Frontend(backend)

if __name__ == "__main__":
    main()