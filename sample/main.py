from sys import argv
import UI
import EntityHandler
import ListGenerator
import Location
from ItemFactory import ItemFactory

# Main Loop
def main(args = argv[1:]):
    # Object Variables
    entityHandler = EntityHandler.EntityHandler()
    location = Location.Location()
    listGenerator = ListGenerator.ListGenerator("", entityHandler, location)
    userInterface = UI.UI(entityHandler, listGenerator, location)
    
    entityHandler.addEntity(ItemFactory("Item A", "Item", {"College": "A1"}))
    entityHandler.addEntity(ItemFactory("Recipe A", "ItemContainer", ["Item A"]))
    
    
    # debug = False

    # for arg in args:
    #     match arg:
    #         case "-d":
    #             debug = True
    #         case _:
    #             raise ValueError(f"Invalid argument: {arg}")

    # backend = Backend.Backend(debug=debug)
    # Frontend.Frontend(backend)
    
if __name__ == "__main__":
    main()