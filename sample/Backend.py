from pyperclip import copy

class Backend:
    # NOTE: I may be able to get away with an abstract class because of how similar the recipe and item functions are
    def __init__(self, filename="grocery_list.txt", debug=False):
        self.filename = filename
        self.raw_list = []
        self.debug

        try:
            with open(self.filename, "r", encoding="utf-8") as f:   
                self.raw_list = f.read().splitlines()
        except FileNotFoundError:
            f = open(self.filename, "a+", encoding="utf-8")
            f.write("")

        self.final_list = []
        self.items = [entry for entry in self.raw_list if entry.startswith("I:")]
        self.recipes = [entry for entry in self.raw_list if entry.startswith("R:")]
        self.locations = ["college", "grandparents", "jordan"]
        self.current_location = self.locations[0]

        if self.debug:
            self.debug()
             
    def close(self, root):
        with open(self.filename, "w", encoding="utf-8") as f:
            f.write("\n".join(self.items + self.recipes))

        if self.debug:
            self.debug()

        root.destroy()
    
    def debug(self):
        list_headers = ["Raw List", "Items", "Recipes", "Locations", "Final List"]
        all_lists = [self.raw_list, self.items, self.recipes, self.locations, self.final_list]
        
        print("Path:", self.filename)
        print("Current Location:", self.current_location)

        for i in range(len(list_headers)):
            print(f"--{list_headers[i]}--")

            for element in all_lists[i]:
                print(element)

    def get_item_index(self, query):
        item_names = [entry[2:].split('|')[0] for entry in self.items]

        return item_names.index(query)

    def get_item_names(self, query=None):
        item_names = [entry[2:].split('|')[0] for entry in self.items]

        return item_names if query == None else item_names[self.get_item_index(query)]

    def get_item_aisles(self, query=None):
        index = self.locations.index(self.current_location)
        item_aisles = [entry[2:].split('|')[index + 1] for entry in self.items]

        return item_aisles if query == None else item_aisles[self.get_item_index(query)]

    def add_item(self, entry):
        self.items.append(entry)

    def edit_item(self, entry):
        self.delete_item(self.get_item_names(entry))
        self.add_item(entry)

    def delete_item(self, name):
        self.items.pop(self.get_item_index(name))
    
    def get_recipe_index(self, query):
        recipe_names = [entry[2:].split('|')[0] for entry in self.recipes]

        return recipe_names.index(query)

    def get_recipe_names(self, query=None):
        recipe_names = [entry[2:].split('|')[0] for entry in self.recipes]

        return recipe_names if query == None else recipe_names[self.get_recipe_index(query)]

    def get_recipe_items(self, query=None):
        recipe_items = [entry[2:].split('|')[1] for entry in self.recipes]

        return recipe_items if query == None else recipe_items[self.get_recipe_index(query)]

    def add_recipe(self, entry):
        items = entry.split('|')[1].split(',')
        
        for item in items:
            if item not in self.get_item_names():
                print(f"{item} missing!", f"{item} does not exist. Please add and configure {item} first.")

        self.recipes.append(entry)

    def edit_recipe(self, name):
        self.delete_recipe(self.get_recipe_names(name))
        self.add_recipe(entry)

    def delete_recipe(self, name):
        self.recipes.pop(self.get_recipe_names(name))

    def generate_list(self, user_list):
        self.final_list = []
        user_list = user_list.split('\n')

        for entry in user_list:
            if self.debug:
                print(f"Searching for {entry} with location '{self.current_location}'...")

            try:
                self.get_item_names(entry)
            except ValueError:
                try:
                    self.get_recipe_names(entry)
                except ValueError:
                    self.final_list.append(f"Entry '{entry}' not found!")
                else:
                    for item in self.get_recipe_items(entry).split(','):
                        if self.debug:
                                print(f"Found {item}!")
                            
                        # - [ ] (1A) Item Name
                        entry = f"- [ ] ({self.get_item_aisles(item)}) "
                        print(entry)
                        entry = entry + f"{self.get_item_names(item)}"
                        print(entry)
                        self.final_list.append(entry)     
            else:
                if self.debug:
                    print(f"Found {entry}!")
                
                item = f"- [ ] ({self.get_item_aisles(entry)}) "
                print(item)
                item = item + f"{self.get_item_names(entry)}"
                print(item)
                self.final_list.append(item)
                

        # TODO: Identify list type to organize accordingly
        # Sort list alphanumerically
        print(self.final_list)
        self.final_list.sort(key=lambda x: (
            # Numbers
            int(x[7:].split(')')[0][:-1]),
            # Letters
            x[7:].split(')')[0][-1]
        ))

        copy('\n'.join(self.final_list))

    def get_locations(self):
        return self.locations
    
    def set_location(self, location):
        self.current_location = location
