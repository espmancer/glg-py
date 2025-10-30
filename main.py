import Frontend, Backend        
# Main Loop
def main():
    backend = Backend.Backend()
    print(backend.get_item_lists())
    
    Frontend.Frontend(backend)

if __name__ == "__main__":
    main()