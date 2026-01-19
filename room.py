# Define the Room class.
from config import DEBUG
class Room:

    # Define the constructor. 
    def __init__(self, name, description, character):
        self.name = name
        self.description = description
        # Exits doivent être un dictionnaire de directions -> Room
        self.exits = {}
        self.interactions = {}   # <-- Dictionnaire des objets interactifs
        self.inventory = {}     # objets
        self.characters =  {}        #PNJ
    
    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"
    
    def get_inventory(self):
        if not self.inventory and not self.characters:
            print("\nIl n'y a rien ici.")
            return
        print("\nOn voit :")
        for item in self.inventory.values():
            print(f"    - {item.name} : {item.description} ({item.weight} kg)")
        for character in self.characters.values():
            print(f"    - {character.name} : {character.description}\n")