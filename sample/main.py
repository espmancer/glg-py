import Frontend, Backend
from sys import argv       

# Main Loop
def main(args = argv[1:]):
    debug = False

    for arg in args:
        match arg:
            case "-d":
                debug = True
            case _:
                raise ValueError(f"Invalid argument: {arg}")

    backend = Backend.Backend(debug=debug)
    Frontend.Frontend(backend)
    
if __name__ == "__main__":
    main()