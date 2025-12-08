# Define the Player class.
class Player():

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.inventory = []
        self.history = ["Hall"]  # Liste des pièces visitées, initialisée avec la pièce de départ
        
    
    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]
        self.current_room = next_room


        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False

        self.history.append(next_room.name)

        print(self.get_history_string())
    
        # Set the current room to the next room.
        print(self.current_room.get_long_description())
        return True

        

    def get_history(self):
        # retourne une liste des pièces déjà visitées
        return self.history
    
    def get_history_string(self):
        # retourne une chaîne comme : "Historique : Cuisine -> Laboratoire -> Couloir"
        return "Historique : " + " -> ".join(self.history)
    
    def go_back(self):
        # retourne à la pièce précédente si possible
        if len(self.history) > 1:
            self.history.pop()  # Enlève la pièce actuelle
            previous_room_name = self.history[-1]
            return previous_room_name
        return None
        