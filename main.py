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
        print(f"{i} - {item_list[i]["name"]}")

def delete_item():
    set_item_index(int(input("Choose 1 number from the list of items: ")))
    item_list.remove(current_item_index)
    set_item_index(0)

def edit_item():
    list_items()
    set_item_index(int(input("Choose 1 number from the list of items: ")))
    for key in item_list[current_item_index]:
        print(item_list[current_item_index][key])





edit_item()