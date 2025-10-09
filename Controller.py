item_list = [{
  "name":"Element Name",
  "type":"item",
  "aisle": {
    "College":"A1",
    "Grandparents":"A2",
    "Jordan":"A3"
  }
}]
current_item_index = 0
locations = ["College", "Grandparents", "Jordan"]
# Functions
def set_item_index(index):
    global current_item_index
    current_item_index = index
def add_item():
    item_name = input("Enter item name: ")
    aisles = {location: input(f"Enter aisle for '{location}': ") for location in locations}
    item_list.append({
                        "name":item_name,
                        "type":"item",
                        "aisle":aisles
                    })
    set_item_index(len(item_list) - 1)
def list_items():
    for i in range(len(item_list)):
        print(f"{i} - {item_list[i]['name']}")
def delete_item():
    set_item_index(int(input("Choose 1 number from the list of items: ")))
    print(f"Deleted {item_list[current_item_index]['name']}.")
    item_list.remove(current_item_index)
    set_item_index(0)
def edit_item():
    list_items()
    set_item_index(int(input("Choose 1 number from the list of items: ")))
    print("0 - Name")
    print("1 - Aisles")
    choice = int(input("Choose 1 number from the list of options: "))
    if choice == 0:
        print("Current Name:", item_list[current_item_index]['name'])
        item_list[current_item_index]['name'] = input("New Name: ")
    elif choice == 1:
        for location in range(len(locations)):
            print(f"{location} - {locations[location]}")
        choice = int(input("Choose 1 number from the list of options: "))
        print(f"Current Aisle of {locations[choice]}: {item_list[current_item_index]['aisle'][locations[choice]]}")
        item_list[current_item_index]['aisle'][locations[choice]] = input("New Aisle: ")
# Main Function
def main():
  edit_item()
  print(item_list)    
# Run Main
main()