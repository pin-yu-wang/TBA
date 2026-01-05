# Define the Character class.
import random
from config import DEBUG
class Character():

    def __init__(self, name, description, current_room, msgs):
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs
    
    def __str__(self):
        return f"{self.name} : {self.description}"
    
    def move(self):
        # 1 chance sur 2 de rester sur place
        if random.choice([True, False]) is False:
            if DEBUG:
                print(f"[DEBUG] {self.name} reste dans {self.current_room.name}")
            return False

        # Récupérer uniquement les pièces adjacentes valides (non None)
        neighbors = [r for r in self.current_room.exits.values() if r is not None]
        if not neighbors:
            if DEBUG:
                print(f"[DEBUG] {self.name} ne peut pas se déplacer (aucune sortie valide).")
            return False

        # Choisir aléatoirement une pièce parmi les voisins valides
        new_room = random.choice(neighbors)

        if DEBUG:
            print(f"[DEBUG] {self.name} se déplace de {self.current_room.name} à {new_room.name}")

        # Retirer le personnage de la pièce actuelle en toute sécurité
        self.current_room.characters.pop(self.name, None)

        # Ajouter le personnage à la nouvelle pièce et mettre à jour sa position
        new_room.characters[self.name] = self
        self.current_room = new_room
        return True
    

    
    def get_msg(self):
        if self.msgs:
            msg = self.msgs.pop(0)
            print(f"{self.name} dit : \"{msg}\"")
        else:
            print(f"{self.name} dit : \"Je n'ai plus rien à dire.\"")
        
