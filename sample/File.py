"""
File
This class is designed to read and write to the grocery_list.txt file.
"""
class File():
    def __init__(self, path="grocery_list.txt"):
        self.path = path
        self.f = None

        self.openOrCreateFile()

    # See if there is a file at the provided path, create one if there isn't.
    def openOrCreateFile(self):
        try:
            self.f = open(self.path, "rw")
        except FileNotFoundError:
            with open(self.path, "a+") as self.f:
            self.f.write("")

    # Get all contents of the file at the provided path.
    def readFile(self) -> str:
        return self.f.read()

    def writeFile(self, string):
        self.f.write(string)

