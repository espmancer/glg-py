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

add_item()
print(item_list[current_item_index])
