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
        self.entities.update({entity.name: entity})
    
    # Remove one object at key from the entities dictionary.
    def removeEntity(self, key):
        del self.entities[key]
    
    # Set one object's value to another object at key in the entities dictionary.
    def editEntity(self, key, entity):
        self.entities[key] = entity

    # Get one object's value at key from the entities dictionary.
    def getEntity(self, key) -> object:
        return self.entities[key]

    # Get all objects from the entities dictionary.
    def getEntities(self) -> list:
        return self.entities