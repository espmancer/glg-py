"""
Location
This class is designed to add, remove, and manipulate an n-sized list of locations.
This class is also designed to get and set a current location.
"""
class Location():
    def __init__(self, locations=["Location 1"], currentLocation="Location 1"):
        self.locations = locations
        self.currentLocation = currentLocation 

    # Add one location to the locations list.
    def addLocation(self, location):
        self.locations.add(location)

    # Remove one location at index from the locations list.
    def removeLocation(self, index):
        self.locations.pop(index)

    # Set one location's value to another location at index in the locations list.
    def editLocation(self, index, location):
        self.locations[index] = location

    # Set currentLocation's value to another location at index in the locations list.
    def setCurrentLocation(self, index):
        self.currentLocation = self.locations[index]

    # Get a list of all of the locations.
    def getLocations(self) -> list:
        return self.locations

    # Get the currentLocation.
    def getCurrentLocation(self) -> str:
        return self.currentLocation