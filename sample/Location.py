"""
Location
This class is designed to add, remove, and manipulate
an n-sized list of locations.
"""
class Location():
    def __init__(self, locations=[]):
        self.locations = locations

    # Add one location to the locations list.
    def addLocation(self, location):
        self.locations.add(location)

    # Remove one location at index from the locations list.
    def removeLocation(self, index):
        self.locations.pop(index)

    # Set one location's value to another location at index in the locations list.
    def editLocation(self, index, location):
        self.locations[index] = location