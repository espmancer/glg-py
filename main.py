# NOTE: Temporary one-file version of the code until I can figure out how to refactor it. 
import tkinter as tk

# Locations
locations = ['College', 'Grandparents', 'Jordan']

# Main Screen #
root = tk.Tk()
root.title("GLG")
root.title("GLG")
root.minsize(200, 200)
root.maxsize(500, 500)
root.geometry("300x300+50+50")

## Main Screen Widgets ##
options_rows = 3
options_columns = 3
for columns in range(options_columns):
    root.columnconfigure(columns, weight = 1)

    for rows in range(options_rows):
        root.rowconfigure(rows, weight = 1)
                    
### Items ###
# Item List
item_list = [{"name":"Element Name","type":"item","aisle": {"College":"A1","Grandparents":"A2","Jordan":"A3"}}]
item_names = [item['name'] for item in item_list]
item_listbox = tk.Listbox(root)

for item in item_names:
    item_listbox.insert(tk.END, item)

item_listbox.grid(column = 0, row = 0, rowspan = 3)

# Add Item
def add_item():
    open_item_screen('add')
add_item_btn = tk.Button(root, text = "Add Item", command = add_item)
add_item_btn.grid(column = 1, row = 0, padx = 3)

# Edit Item
edit_item_btn = tk.Button(root, text = "Edit Item")
edit_item_btn.grid(column = 1, row = 1, padx = 3)

# Remove Item
remove_item_btn = tk.Button(root, text = "Remove Item")
remove_item_btn.grid(column = 1, row = 2, padx = 3)

# Recipes #
# Add Recipe
add_recipe_btn = tk.Button(root, text = "Add Recipe")
add_recipe_btn.grid(column = 2, row = 0)

# Edit Recipe 
edit_recipe_btn = tk.Button(root, text = "Edit Recipe")
edit_recipe_btn.grid(column = 2, row = 1)

# Remove Recipe
remove_recipe_btn = tk.Button(root, text = "Remove Recipe")
remove_recipe_btn.grid(column = 2, row = 2)

## Item Screen ##
def open_item_screen(save_type):
    item_screen = tk.Toplevel(root)
    item_screen.title("GLG")
    item_screen.title("GLG")
    item_screen.minsize(200, 200)
    item_screen.maxsize(500, 500)
    item_screen.geometry("200x200+100+100")
    
    # Item Attribute Grid 
    options_rows = 2 + len(locations)
    options_columns = 2
    for columns in range(options_columns):
        root.columnconfigure(columns, weight = 1)
    
        for rows in range(options_rows):
            root.rowconfigure(rows, weight = 1)
    
    # Item Name 
    item_name_lbl = tk.Label(item_screen, text = "Item Name")
    item_name_lbl.grid(column = 0, row = 0)
    item_name_etr = tk.Entry(item_screen)
    item_name_etr.grid(column = 1, row = 0)
    # Item Aisles 
    aisle_lbls = []
    aisle_etrs = []
    current_row = 1
    
    for location in locations:
        aisle_lbls.append(tk.Label(item_screen, text = location + " Aisle"))
        aisle_etrs.append(tk.Entry(item_screen))
        aisle_lbls[current_row - 1].grid(column = 0, row = current_row)        
        aisle_etrs[current_row - 1].grid(column = 1, row = current_row)
        current_row += 1
    # Save Button
    # TODO: Figure out why the button text doesn't center
    save_btn = tk.Button(item_screen, text = "Save", width = 3, anchor = "w", command = lambda: save_item(item_name_etr, aisle_etrs, save_type))
    save_btn.grid(columnspan = 2, row = options_rows, sticky = 'nsew')
    
def save_item(item_name_etr, aisle_etrs, save_type):
    global item_list
    if save_type == 'edit':
        item_list = [item for item in item_list if item["name"] != item_name_etr.get()]
    
    item_list.append({
            "name": item_name_etr.get(),
            "type": "item",
            "aisle": {location: entry.get() for location, entry in zip(locations, aisle_etrs)}
        })    
            
# Close program and save to txt
def save_and_close():
    print("Saved!")
    root.destroy()
    
# Main Loop
root.protocol("WM_DELETE_WINDOW", save_and_close)
root.mainloop()
