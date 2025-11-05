import tkinter as tk
from tkinter import ttk, messagebox

class Frontend:
    def __init__(self, backend, root=tk.Tk()):
        self.backend = backend
        self.root = root

        root.title("GLG")
        root.minsize(300, 350)
        root.geometry("300x350+50+50")
        root.protocol("WM_DELETE_WINDOW", lambda: self.backend.close(root))

        # Main Menu (Notebook)
        tab_ntbk = ttk.Notebook(root)
        tab_ntbk.pack(fill="both", expand=True)
        tab_ntbk.bind('<<NotebookTabChanged>>', lambda event: self.update_lists())
        
        # Frames
        list_frame = tk.Frame(tab_ntbk)
        item_frame = tk.Frame(tab_ntbk)
        recipe_frame = tk.Frame(tab_ntbk)
        location_frame = tk.Frame(tab_ntbk)

            # Add Frames
        tab_ntbk.add(list_frame, text="List")
        tab_ntbk.add(item_frame, text="Items")
        tab_ntbk.add(recipe_frame, text="Recipes")
        tab_ntbk.add(location_frame, text="Locations")

        # List Frame layout
        list_frame.columnconfigure(0, weight=1)
        list_frame.columnconfigure(1, weight=1)
        list_frame.rowconfigure(0, weight=1)

            # User List (Text Widget)
        user_list = tk.Text(list_frame, width=25)
        user_list.grid(column=0, row=0, sticky="nsew", padx=5, pady=5)

            # Generate List Button
        generate_list_btn = tk.Button(list_frame, text="Generate List", command=lambda: (
            self.backend.generate_list(user_list.get("1.0", "end-1c")),
            messagebox.showinfo("Notice", "List has been copied to clipboard.")))
        generate_list_btn.grid(column=1, row=0, sticky="nsew", padx=5, pady=5)

            # Item Frame
                # Item Listbox
        self.item_lbox = tk.Listbox(item_frame, listvariable=self.backend.get_item_lists())
        self.item_lbox.bind('<<ListboxSelect>>', self.select_item)
        
                # Item Name
        item_name_lbl = tk.Label(item_frame, text="Item Name:")
        self.item_name_etr = tk.Entry(item_frame)
        
                # College Aisle
        college_aisle_lbl = tk.Label(item_frame, text="College Aisle:")
        self.college_aisle_etr = tk.Entry(item_frame)
        
                # Grandparents Aisle
        grandparents_aisle_lbl = tk.Label(item_frame, text="Grandparents Aisle:")   
        self.grandparents_aisle_etr = tk.Entry(item_frame)
        
                # Jordan Aisle
        jordan_aisle_lbl = tk.Label(item_frame, text="Jordan Aisle:")
        self.jordan_aisle_etr = tk.Entry(item_frame)
        
                # Add Item Button
        add_item_btn = tk.Button(item_frame, text="Save New Item", command=lambda: (
            self.backend.add_item(
                f"I:{self.item_name_etr.get()}|{self.college_aisle_etr.get()}|{self.grandparents_aisle_etr.get()}|{self.jordan_aisle_etr.get()}"
            ),
            self.update_lists()))

                # Edit Item Button
        edit_item_btn = tk.Button(item_frame, text="Save Item", command=lambda: (self.backend.edit_item(
            int(self.item_lbox.curselection()[0]),
            f"I:{self.item_name_etr.get()}|{self.college_aisle_etr.get()}|{self.grandparents_aisle_etr.get()}|{self.jordan_aisle_etr.get()}"),
            self.update_lists()))
        
                # Delete Item Button
        delete_item_btn = tk.Button(item_frame, text="Delete Item", command=lambda: (self.backend.delete_item(self.item_name_etr.get()), self.update_lists()))

        """
        |Listbox [0][0]|Item Name Label    [1][0]|Item Name Entry          [1][0]|
        |      | [0][1]|College Label      [1][1]|College Aisle Entry      [1][1]|
        |      | [0][2]|Grandparents Label [1][2]|Grandparents Aisle Entry [1][2]|
        |      | [0][3]|Jordan Label       [1][3]|Jordan Aisle Entry       [1][3]|
        |Add Item Button                                                 [0-2][4]|
        |Edit Item Button                                                [0-2][5]|
        |Delete Item Button                                              [0-2][6]|
        """
        for col in range(3):
            item_frame.columnconfigure(col, weight=1)
            for row in range(7):
                item_frame.rowconfigure(row, weight=1)
        
        # Item Listbox [Col 0]
        self.item_lbox.grid(column=0, row=0, rowspan=4)
        
        # Labels [Col 1]
        item_name_lbl.grid(column=1, row=0)
        grandparents_aisle_lbl.grid(column=1, row=1) 
        college_aisle_lbl.grid(column=1, row=2)
        jordan_aisle_lbl.grid(column=1, row=3)
        
        # Entries [Col 2]
        self.item_name_etr.grid(column=2, row=0)
        self.college_aisle_etr.grid(column=2, row=1)
        self.grandparents_aisle_etr.grid(column=2, row=2)
        self.jordan_aisle_etr.grid(column=2, row=3)

        # Buttons [Col 0-2]
        add_item_btn.grid(column=0, row=4, columnspan=3)
        edit_item_btn.grid(column=0, row=5, columnspan=3)
        delete_item_btn.grid(column=0, row=6, columnspan=3)

            # Recipe Frame
        """
        
        """
        for col in range(2):
            recipe_frame.columnconfigure(col, weight=1)
            for row in range(4):
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
        self.recipe_name_etr.grid(column=1, row=3)

                # Recipe Items List (Text Widget)
        recipe_items_lbl = tk.Label(recipe_frame, text="Recipe Items")
        recipe_items_lbl.grid(column=0, row=3)
        self.recipe_items_list = tk.Text(recipe_frame, height=5, width=10)
        self.recipe_items_list.grid(column=1, row=3)

                # Add Recipe Button
        newline = '\n'
        add_recipe_btn = tk.Button(recipe_frame, text="Save New Recipe", command=lambda: (self.backend.add_recipe(
            f"R:{self.recipe_name_etr.get()}|{self.recipe_items_list.get('1.0', 'end-1c').replace(newline, ',')}"
            ), self.update_lists()))
        add_recipe_btn.grid(column=1, row=0)

                # Edit Recipe Button
        edit_recipe_btn = tk.Button(recipe_frame, text="Save Recipe", command=lambda: (self.backend.recipe_item(
            int(self.recipe_lbox.curselection()[0]),
            f"R:{self.recipe_name_etr.get()}|{self.recipe_items_list.get('1.0', 'end-1c').replace(newline, ',')}"),
            self.update_lists()))
        edit_recipe_btn.grid(column=1, row=1)
        
                # Delete Recipe Button
        delete_recipe_btn = tk.Button(recipe_frame, text="Delete Recipe", command=lambda: (self.backend.delete_recipe(self.recipe_name_etr.get()), self.update_lists()))
        delete_recipe_btn.grid(column=1, row=2)

            # Locations Frame
        location_var = tk.StringVar(value=self.backend.current_location)

        # Create the OptionMenu
        location_mnu = tk.OptionMenu(
            location_frame,
            location_var,
            *self.backend.get_locations(),
            command=lambda location: self.backend.set_location(location)
        )
        location_mnu.pack()

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
        last_index = 0
        index = last_index
        
        try:
            index = int(self.item_lbox.curselection()[0])
            last_index = index
        except IndexError:
            index = last_index
            self.item_lbox.selection_set(index)
        else:
            self.set_text(self.item_name_etr, self.backend.get_item_lists("name")[index])
            self.set_text(self.college_aisle_etr, self.backend.get_item_lists("college")[index])
            self.set_text(self.grandparents_aisle_etr, self.backend.get_item_lists("grandparents")[index])
            self.set_text(self.jordan_aisle_etr, self.backend.get_item_lists("jordan")[index])

    def select_recipe(self, event):
        last_index = 0
        index = last_index
        
        try:
            index = int(self.item_lbox.curselection()[0])
            last_index = index
        except IndexError:
            index = last_index
            self.item_lbox.selection_set(index)
        else:
            self.set_text(self.recipe_name_etr, self.backend.get_recipe_lists("name")[index])
            self.set_text(self.recipe_items_list, self.backend.get_recipe_lists("items")[index])

    def set_text(self, entry, text):
        index = "1.0" if isinstance(entry, tk.Text) else 0 
        entry.delete(index, tk.END)
        entry.insert(index, text)
