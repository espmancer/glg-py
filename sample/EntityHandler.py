"""
EntityHandler
This class is designed to add, remove, and manipulate
an n-sized dictionary of Items and ItemContainers.
"""
class EntityHandler():
    def __init__(self, entities={}):
        self.entities = entities

    # Add one object to the entities dictionary.
    def addEntity(self, entity):
        self.entities.add(entity)
    
    # Remove one object at an index from the entities dictionary.
    def removeEntity(self, index):
        self.entities.pop(index)
    
    # Set one object's value to another object at an index in the entities dictionary.
    def editEntity(self, index, entity):
        self.entities[index] = entity
