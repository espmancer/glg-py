# glg-py
A grocery list generator made in [Python](https://www.python.org). Originally I used [Dataview](https://github.com/blacksmithgu/obsidian-dataview) within [Obsidian](https://obsidian.md/) to generate a numerically sorted list of items I linked in another list of recipes. Each entry was its own page with metadata, which got tricky to work with on mobile. After that I tried to make it in using [JSON](https://en.wikipedia.org/wiki/JSON) and a [JSONPath](https://en.wikipedia.org/wiki/JSONPath) addon in [LabVIEW](https://www.ni.com/en/support/downloads/software-products/download.labview.html#570679) called [JSONText](https://www.vipm.io/package/jdp_science_jsontext/), but I suddenly needed to fix problems in that [JSONText](https://www.vipm.io/package/jdp_science_jsontext/) library in order to get it to do what I wanted, so I switched to [Python](https://www.python.org) and [Tkinter](https://docs.python.org/3/library/tkinter.html) instead.
## How It Works
- This program uses and manipulates a list multi-delimited strings stored in a txt file within the application.
- There are functions to add, remove, and edit these strings.
- Once the list is configured, an alphanumerically sorted list of items and their aisles is created, with each item having the markdown checkbox.
  - [ ] Like this
## To Run
1. Download zip.
2. Extract zip to desired folder.
3. Go into glg-1.0/dist
4. Run "main.exe"
### Items
Items are the most concrete level of elements in the list. They contain a name and three aisles, which is formatted as such:
```
I:Example Item|A1|A2|A3
```
Currently the aisles are hardcoded and are specific to Walmart's aisle system, but I may add functionality to add and edit stores and their particular locations.  
### Recipes
Recipes are lists of items. They contain a name and delimited string of items, and are formatted as such:
```
R:Example Recipe|Item A, Item B
```
## Future Ideas
- I may try and make this compatible with mobile and remove a computer from the equation altogether. Python has an [Android library](https://pypi.org/project/python-for-android/) that I might be able to use.
- As mentioned before, locations may be configurable in the future.
<<<<<<< HEAD
<<<<<<< HEAD
- Abstract "Configurables" class that items and recipe classes can override
=======
- Options to format the final list to a specific app (e.g. To Do, Keep, Obsidian)
>>>>>>> 0e00ed7 (Add app config idea)
=======
- Options to format the final list to a specific app (e.g. To Do, Keep, Obsidian)
>>>>>>> refs/remotes/origin/main
