"""
File
This class is designed to read and write to the grocery_list.txt file.
"""
class File():
    def __init__(self, path="grocery_list.txt"):
        self.path = path

        self.openOrCreateFile()

    # See if there is a file at the provided path, create one if there isn't.
    def openOrCreateFile(self):
        try:
            open(self.path, "r")
        except FileNotFoundError:
            with open(self.path, "a+") as f:
                f.write("")

    # Get all contents of the file at the provided path.
    def readFile(self) -> str:
        with open(self.path, "r") as f:
            return f.read()

    # Set all contents of the file at the provided path.
    def writeFile(self, string):
        with open(self.path, "w") as f:
            f.write(string)
