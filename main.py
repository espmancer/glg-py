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
        self.recipes = [entry for entry in self.raw_list if entry.startswith("R:")]
        self.locations = ["College", "Grandparents", "Jordan"]
           
    def close(self):
        self.raw_list = self.items + self.recipes
        print("Closing!")
        with open(self.filename, "w", encoding="utf-8") as f:
            f.write("\n".join(self.raw_list))
# Main Loop
def main():
    backend = Backend()
    recipe = backend.build_recipe("Recipe B", ["Item A", "Item C"])
    backend.add_recipe(recipe)
    backend.close()
    # Main Screen #
    root = tk.Tk()
    root.title("GLG")
    root.title("GLG")
    root.minsize(200, 200)
    root.maxsize(500, 500)
    root.geometry("300x300+50+50")
    root.protocol("WM_DELETE_WINDOW", backend.close)
    root.mainloop()

if __name__ == "__main__":
    main()