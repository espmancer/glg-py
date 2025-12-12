"""
ListGenerator
This class is designed as the name entails.
"""
class ListGenerator():
    def __init__(self, userList, entity):
        self.userList = userList
        entityList = entity.getEntities()
        self.finalList = []

