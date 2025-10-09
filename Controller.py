from os import getenv
import App

global debug
debug = True

class Controller:
    def __init__(self, item_list, current_item_index):
        self.current_item_index = 0
        self.locations = ["College", "Grandparents", "Jordan"]
        if debug:
            self.item_list = [{"name":"Element Name","type":"item","aisle": {"College":"A1","Grandparents":"A2","Jordan":"A3"}}]
        else:
            path = f"{getenv('LOCALAPPDATA')}\\GLG\\grocery_list.txt"
            self.item_list = open(path, "r").read() 
    def add_item(self):
        item_name = input("Enter item name: ")
        aisles = {location: input(f"Enter aisle for '{location}': ") for location in self.locations}
        self.item_list.append({
                            "name":item_name,
                            "type":"item",
                            "aisle":aisles
                        })
        self.current_item_index = 0
    def list_items(self):
        for i in range(len(self.item_list)):
            print(f"{i} - {self.item_list[i]['name']}")
    def delete_item(self):
        self.current_item_index = int(input("Choose 1 number from the list of items: "))
        print(f"Deleted {self.item_list[self.current_item_index]['name']}.")
        self.item_list.remove(self.current_item_index)
        self.current_item_index = 0
    def edit_item(self):
        self.list_items()
        self.current_item_index = int(input("Choose 1 number from the list of items: "))
        print("0 - Name")
        print("1 - Aisles")
        choice = int(input("Choose 1 number from the list of options: "))
        if choice == 0:
            print("Current Name:", self.item_list[self.current_item_index]['name'])
            self.item_list[self.current_item_index]['name'] = input("New Name: ")
        elif choice == 1:
            for location in range(len(self.locations)):
                print(f"{location} - {self.locations[location]}")
            choice = int(input("Choose 1 number from the list of options: "))
            print(f"Current Aisle of {self.locations[choice]}: {self.item_list[self.current_item_index]['aisle'][self.locations[choice]]}")
            self.item_list[self.current_item_index]['aisle'][self.locations[choice]] = input("New Aisle: ")