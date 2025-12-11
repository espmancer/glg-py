"""
File
This class is designed to read and write to the grocery_list.txt file.
"""
class File():
    def __init__(self, path="grocery_list.txt"):
        self.path = path

    # See if there is a file at the provided path, create one if there isn't.
    def openOrCreateFile():
        try:
            open(path, "r")
        except FileNotFoundError:
            with open(path, "a+") as f:
                f.write()
