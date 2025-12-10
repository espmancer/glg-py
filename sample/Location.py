"""
Location
This class is designed to add, remove, and manipulate
an n-sized list of locations.
"""
class Location():
    def __init__(self, locations=[]):
        self.locations = locations

    # Add one location
    def addLocation(self, location):
        self.locations.add(location)