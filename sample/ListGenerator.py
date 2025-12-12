"""
ListGenerator
This class is designed as the name entails.
"""
class ListGenerator():
    def __init__(self, userList, entityHandler, location):
        self.userList = userList
        self.entityList = entityHandler.getEntities()
        self.currentLocation = location.getCurrentLocation()
        self.finalList = []

    def generateList(self):
        for entity in self.userList.split():
            if self.entityList[entity].kind == "Item":
                aisle = self.entityList[entity].aisle[self.currentLocation]
                name = self.entityList[entity].name

                self.finalList.add(f"- [ ] ({aisle}) {name}")
            else:
                for item in self.entityList[entity].items:
                    aisle = self.entityList[item].items[self.currentLocation]
                    name = self.entityList[item].name

                    self.finalList.add(f"- [ ] ({aisle}) {name}")
    
    def getList(self) -> list:
        return self.finalList