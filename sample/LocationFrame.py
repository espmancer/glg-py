"""
LocationFrame
This class is designed as the Location configuration screen.
"""
import tkinter as tk

class LocationFrame(tk.Frame):
    def __init__(self, frame, locations=[]):
        super().__init__()

        columnCount = 2
        rowCount = 5

        for column in range(columnCount):
            self.columnconfigure(column, weight=1)
            
            for row in range(rowCount):
                self.rowconfigure(row, weight=1)

        # Location Listbox
        self.locationListbox = tk.Listbox(self, listvariable=locations)
        self.locationListbox.grid(column=0, row=0, rowspan=4)
        # Add Item Button
        self.addLocationButton = tk.Button(self, text="Save New Location", command=lambda: self.event_generate("<<addLocation>>"))
        self.addLocationButton.grid(column=0, row=2, columnspan=3)
        # Edit Item Button
        self.editLocationButton = tk.Button(self, text="Save Location", command=lambda: self.event_generate("<<editLocation>>"))
        self.editLocationButton.grid(column=0, row=3, columnspan=3)
        # Remove Item Button
        self.removeLocationButton = tk.Button(self, text="Remove Location", command=lambda: self.event_generate("<<removeLocation>>"))
        self.removeLocationButton.grid(column=0, row=4, columnspan=3)