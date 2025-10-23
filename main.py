# NOTE: Temporary one-file version of the code until I can figure out how to refactor it. 
import tkinter as tk

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
        print(f"Closing!\nItems:{self.items}\nRecipes:{self.recipes}")
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

class Frontend:
    def __init__(self, backend, root = tk.Tk()):
        self.backend = backend
        self.root = root
        root.title("GLG")
        root.title("GLG")
        root.minsize(200, 200)
        root.maxsize(500, 500)
        root.geometry("300x300+50+50")
        root.protocol("WM_DELETE_WINDOW", lambda: self.backend.close(root))
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