from pyperclip import copy

class Backend:
    # NOTE: I may be able to get away with an abstract class because of how similar the recipe and item functions are
    def __init__(self, filename="grocery_list.txt", debug=False):
        self.filename = filename
        self.raw_list = []a
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

    # TODO: Split this function into multiple parts for better practice, and add a query
    # TODO: Make non-hardcoded locations for this function
    def get_item_lists(self, section=None, query=None):
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

    def edit_item(self, index, entry):
        self.delete_item(self.get_item_lists("name")[index])
        self.add_item(entry)

    def delete_item(self, name):
        self.items.pop(self.get_item_lists("name").index(name))

    def get_recipe_lists(self, section=None, query=None):
        recipe_names = [entry[2:].split('|')[0] for entry in self.recipes]
        recipe_items = [entry.split('|')[1] for entry in self.recipes]
        
        if query == None:
            if section == None:
                return self.recipes
            elif section == "name":
                return recipe_names
            elif section == "items":
                return recipe_items
        else:
            try: 
                index = recipe_names.index(query)
                
                if section == None:
                    return self.recipes[index]
                elif section == "name":
                    return recipe_names[index]
                elif section == "items":
                    return recipe_items[index]
            except ValueError:
                raise ValueError
        
    def add_recipe(self, entry):
        items = entry.split('|')[1].split(',')
        
        for item in items:
            if item not in self.get_item_lists("name"):
                print(f"{item} missing!", f"{item} does not exist. Please add and configure {item} first.")

        self.recipes.append(entry)

    def edit_recipe(self, index, entry):
        self.delete_recipe(self.get_recipe_lists("name")[index])
        self.add_recipe(entry)

    def delete_recipe(self, name):
        self.recipes.pop(self.get_recipe_lists("name").index(name))

    def generate_list(self, user_list):
        self.final_list = []
        user_list = user_list.split('\n')

        # User List will look something like this: [Item A, Recipe A, Item B]
        # Split the recipes into their respective items
        # Remove the recipes and add the split recipes to the user list
        # Get aisle for selected location for each item
        # Format each aisle to each item (- [ ] ({aisle}) {item}) 

        for entry in user_list:
            if self.debug:
                print(f"Searching for {entry} with location '{self.current_location}'...")

            try:
                self.get_item_lists("name").index(entry)  
            except ValueError:
                try:
                    self.get_recipe_lists("name").index(entry)  
                except ValueError:
                    self.final_list.append(f"Entry '{entry}' not found!")
                else:
                    for items in self.get_recipe_lists("items", entry):
                        for item in items.split(','):
                            if self.debug:
                                print(f"Found {item}!")
                            
                            entry = f"- [ ] {self.get_item_lists(self.current_location)[self.get_item_lists('name').index(item)]}) {self.get_item_lists('name')[self.get_item_lists('name').index(item)]}"
                            self.final_list.append(entry)
            else:
                if self.debug:
                    print(f"Found {entry}!")
                
                entry = f"- [ ] ({self.get_item_aisles(self.current_location, item)}) "
                entry = entry + f"{self.get_item_names(item)}"
                self.final_list.append(entry)
                self.final_list.pop(-1)

        # TODO: Identify list type to organize accordingly
        # Sort list alphanumerically
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
