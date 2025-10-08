# glg-py
A grocery list generator made in [Python](https://www.python.org). Originally I used [Dataview](https://github.com/blacksmithgu/obsidian-dataview) within [Obsidian](https://obsidian.md/) to generate a numerically sorted list of items I linked in another list of recipes. Each entry was its own page with metadata, which got tricky to work with on mobile. After that I tried to make it in using [JSON](https://en.wikipedia.org/wiki/JSON) and a [JSONPath](https://en.wikipedia.org/wiki/JSONPath) addon in [LabVIEW](https://www.ni.com/en/support/downloads/software-products/download.labview.html#570679) called [JSONText](https://www.vipm.io/package/jdp_science_jsontext/), but I suddenly needed to fix problems in that [JSONText](https://www.vipm.io/package/jdp_science_jsontext/) library in order to get it to do what I wanted, so I switched to [Python](https://www.python.org) instead.
## How It Works
- This program uses and manipulates a list of dictionaries stored in a txt file within your system's local appdata folder. It will be under a GLG folder if you want to manually edit it for some reason.
- There are functions to add, remove, and edit these dictionaries.
- Once the list is configured, an alphanumerically sorted list of items and their aisles is created, with each item having the markdown checkbox.
  - [ ] Like this
### Items
Items are the most concrete level of elements in the list. They contain a name, type, and set of aisles, which is formatted as such:
```py
{
  "name":"Element Name",
  "type":"item",
  "aisle": {
    "College":"A1",
    "Grandparents":"A2"
  }
}
```
Currently the aisles are hardcoded and are specific to Walmart's aisle system, but I may add functionality to add and edit stores and their particular locations.  
### Recipes
Recipes are lists of items. They contain a name, type, and list of items, and are formatted as such:
```py
{
  "name":"Recipe Name",
  "type":"item",
  "items": [
    "Item A",
    "Item B"
  ]
}
```

