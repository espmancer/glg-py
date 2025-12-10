"""
ItemFactory
This is a dataclass that is designed to follow the Simple Factory design pattern. 
Items contain a name and an n-sized dictionary of aisles based on n number of locations.
"""
@dataclass
class ItemFactory():
    name: str 
    aisles: dict