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
    