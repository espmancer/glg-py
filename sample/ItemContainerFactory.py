"""
ItemContainerFactory
This is a dataclass that is designed to follow the Simple Factory design pattern.
ItemContainers (or Recipes) contain a name and an n-sized dictionary of items.
"""
from dataclasses import dataclass

@dataclass
class ItemContainerFactory:
    name: str
    kind: str
    items: dict