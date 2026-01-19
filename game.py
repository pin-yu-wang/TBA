# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from character import Character
from config import DEBUG
#from game import Game

class Game:
    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.quests = {"item_quest": {
            "completed": False,
            "item": "clé maître",
            "room": "Laboratoire"
        },
        "movement_quest": {
            "completed": False,
            "room": "Laboratoire"
        },
        "interaction_quest": {
            "completed": False,
            "pnj": "gardien"
        }}
        self.commands = {}
        self.player = None
        self.item = []

    def game_turn(self):
        # Assurer qu'un PNJ ne bouge qu'une seule fois par tour :
        seen_ids = set()
        for room in self.rooms:
            for character in list(room.characters.values()):
                # Ignorer si déjà traité ce tour
                if id(character) in seen_ids:
                    continue
                seen_ids.add(id(character))

                moved = character.move()

                if DEBUG:
                    if moved:
                        print(f"[DEBUG] → {character.name} a changé de pièce.")
                    else:
                        print(f"[DEBUG] → {character.name} n'a pas bougé.")

    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)", Actions.go, 1)
        self.commands["go"] = go
        inspect = Command("inspect", " <objet> : inspecter un élément dans la pièce", Actions.inspect, 1)
        self.commands["inspect"] = inspect
        inventory = Command("inventory", " : afficher l'inventaire", Actions.get_inventory, 0)
        self.commands["inventory"] = inventory
        history = Command("history", " : afficher la liste des pièces visitées", Actions.history, 0)
        self.commands["history"] = history
        back = Command("back", " : revenir à la pièce précédente", Actions.back, 0)
        self.commands["back"] = back
        look = Command("look", " : regarder autour de soi pour voir les objets dans la pièce", Actions.look, 0)
        self.commands["look"] = look
        take = Command("take", " <objet> : prendre un objet dans la pièce", Actions.take, 1)
        self.commands["take"] = take
        drop = Command("drop", " <objet> : déposer un objet de l'inventaire dans la pièce", Actions.drop, 1)
        self.commands["drop"] = drop
        check = Command("check", " <objet> : vérifier un objet de l'inventaire", Actions.check, 1)
        self.commands["check"]= check
        talk = Command("talk", " <personnage> : parler à un personnage dans la pièce", Actions.talk, 1)
        self.commands["talk"]= talk

        # Setup rooms

        Hall = Room("Hall", "actuellement dans le Hall, on constate qu'il y a des ecaliers qui mènent vers un étage supérieur.", None)
        self.rooms.append(Hall)
        Salon = Room("Salon", "dans le Salon, plongé dans une pénombre frissonnante, était rempli de meubles anciens recouverts de draps poussiéreux. On constate la présence d'une femme et une échelle à côté d'elle qui mène vers l'étage au-dessus.", "femme")
        self.rooms.append(Salon)
        Bibliothèque = Room("Bibliothèque", "dans la Bibliothèque, saturée d'un parfum de vieux parchemin, alignait ses étagères grinçantes dans une obscurité inquiétante. On observe un grimoire et un doudou au sol, et un mur gravé d'un langage ancien. Il y a une échelle qui vous mène vers l'étage en-dessous.", None)
        self.rooms.append(Bibliothèque)
        Chambre = Room("Chambre", "dans la Chambre, figée dans une lueur blafarde, dévoilait un lit et des rideaux immobiles, sous le lit, il se trouve un coffre vérrouillé, et un enfant assis sur ce dernier, dans le coin de la pièce, vous observez des escaliers qui mènent vers un étage en-dessous.", "enfant")
        self.rooms.append(Chambre)
        Salle_de_musique = Room("Salle_de_musique", "dans la Salle de musique, résonnait d'un silence oppressant, où un piano délaissé semblait attendre que les mains invisibles rejouent une mélodie oubliée, à coté du piano, il se trouve une ps5.", None)
        self.rooms.append(Salle_de_musique)
        Bureau = Room("Bureau", "dans le Bureau, encombré de papiers jaunis et d'un large secrétaire craquant, baignait dans une atmosphère lourde, il y a un tableau poussiéreux sur le mur.", None)
        self.rooms.append(Bureau)

        Laboratoire = Room("Laboratoire", "dans le Laboratoire, déserté, rempli d’appareils silencieux et de fioles encore tièdes, semble figé au milieu d’une expérience interrompue. Il y a une porte verrouillée......", None)
        self.rooms.append(Laboratoire)
        Cuisine = Room("Cuisine", "dans la Cuisine, il y a des casseroles encore chaudes traînant sur le comptoir comme si quelqu’un était parti en plein milieu d’une préparation. En dessous de l’évier, un coffre maître robuste attire votre attention.", None)
        self.rooms.append(Cuisine)



        # Setup interactions and inventories for rooms
        Hall.inventory = {"lettre": Item("lettre", "une lettre ancienne", 0.03)}
        Hall.interactions = {"enfant": Actions.inspecter_enfant,
                             "femme": Actions.femme}


        Bibliothèque.interactions = {"mur": Actions.enigme_maths,
                                    "grimoire": Actions.inspecter_grimoire,
                                    "enfant": Actions.inspecter_enfant,
                                    "femme": Actions.femme}
                
        Bibliothèque.inventory = {"doudou": Item("doudou", "un jouet en peluche", 0.5),
                                "grimoire": Item("grimoire", "un vieux livre poussiéreux rempli de formules mathématiques", 11),
                                "mur" : Item("mur", "un mur avec des inscriptions mystérieuses", 900)}
        

        Bureau.interactions = {"tableau": Actions.inspecter_tableau,
                               "enfant": Actions.inspecter_enfant,
                               "femme": Actions.femme}
        Bureau.inventory = {"tableau": Item("tableau", "un tableau ancien représentant un paysage sombre", 20)}


        Chambre.interactions = {"coffre": Actions.ouvre_coffre,
                                "enfant": Actions.inspecter_enfant,
                                "femme": Actions.femme}
        Chambre.inventory = {"coffre": Item("coffre", "un coffre en bois massif avec un verrou complexe", 20)}
        Chambre.characters = {"enfant": Character("enfant"," un petit garçon aux yeux tristes", Chambre, ["Je m'ennuie tout seul ici", "Voulez-vous jouer avec moi ? Si oui, inspecte-moi"])}
        
        Salle_de_musique.interactions = {"piano": Actions.inspecter_piano,
                                         "enfant": Actions.inspecter_enfant,
                                         "femme": Actions.femme}
                                              
        Salle_de_musique.inventory = {"ps5": Item("ps5", "une console de jeu", 4),
                                      "piano": Item("piano", "un vieux piano à queue", 150)}


        Salon.interactions = {"femme": Actions.femme,
                              "enfant": Actions.inspecter_enfant}
        Salon.characters = {"femme": Character("femme","une silhouette féminine vêtue d'une robe blanche flottante", Salon, ["J'adore les accessoires luxueux !", "Avez-vous quelques choses de précieux à me donner? Si oui, inspecte-moi !"])}
       
        Cuisine.interactions = {"coffre_maître" : Actions.coffre_clé,
                                "enfant": Actions.inspecter_enfant,
                                "femme": Actions.femme}
        Cuisine.inventory = {"coffre_maître": Item("coffre_maître", "un coffre robuste nécessitant une clé spéciale", 30)}


        #Laboratoire.inventory = {"porte": Item("porte","une porte verrouillée", 50)} 



        # Create exits for rooms
        # 1er étage

        Bibliothèque.exits = {"N" : None, "E" : None, "S" : Laboratoire, "O" : Salle_de_musique, "U": None, "D": Salon}
        Chambre.exits = {"N" : Salle_de_musique, "E" : Laboratoire, "S" : None, "O" : None, "U": None, "D": Hall}
        Salle_de_musique.exits = {"N" : None, "E" : Bibliothèque, "S" : Chambre, "O" : None, "U":None, "D": Bureau}
        Laboratoire.exits = {"N" : Bibliothèque, "E" : None, "S" : None, "O" : Chambre,"U":None, "D": Cuisine}


        # rez_de_chaussé
        Hall.exits = {"N" : Bureau, "E" : Cuisine, "S" : None, "O" : None, "U": Chambre, "D":None}
        Salon.exits = {"N" : None, "E" : None, "S" : Cuisine, "O" : Bureau, "U": Bibliothèque, "D": None}
        Bureau.exits = {"N" : None, "E" : Salon, "S" : Hall, "O" : None,"U":Salle_de_musique, "D": None}
        Cuisine.exits = {"N" : Salon, "E" : None, "S" : None, "O" : Hall,"U":Laboratoire, "D": None}

        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = Hall

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Initialiser le timer

        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
            # After each player command, let NPCs take their turns
            self.game_turn()
            self.update_quests(self.player)
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:
        
        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans Alice In Borderland !\n\nIl y a une lettre posée sur la table écrivant 'Boooooh 👻👻👻, vous êtes dans un manoir hanté qui a été fondé en 1879. Si vous ne sortez pas par la porte de sortie qui se trouve quelque part dans ce manoir à temps, vous resterez prisonnier à jamais....... Je vous souhaite bon courage !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())

    def update_quests(self,player):

        #game_running = True

        # Quête d'item : le joueur doit avoir la clé maître dans le laboratoire
        if player.current_room.name == "Laboratoire" and "clé maître" in player.inventory:
            self.quests["item_quest"]["completed"] = True

        # Quête de déplacement : atteindre le laboratoire
        if player.current_room.name == "Laboratoire":
            self.quests["movement_quest"]["completed"] = True

        # Quête d'interaction : parler à l'enfant
        if player.has_talked_to("enfant"):  # <-- adapte selon ton code !
            self.quests["interaction_quest"]["completed"] = True
        # Vérifier les conditions de défaite
        if self.loose(player):
            print(f"\n💀 Dommage {player.name}... Vous êtes entré dans le laboratoire sans la clé maître. Vous restez prisonnier.....vous avez perdu le jeu.\n")
            self.finished = True
            return
        # Vérifier les conditions de victoire
        if self.win():
            print(f"\n🎉 Félicitation {player.name} ! Vous avez réussi ! La porte s'ouvre lentement....Vous êtes maintenant en liberté ! Vive le python 🐍")
            self.finished = True


    # le joueur gagne s'il complète toutes les quêtes
    def win(self):
        return all(quest["completed"] for quest in self.quests.values())

    # le joueur perd s'il entre dans le laboratoire sans avoir la clé maître
    def loose(self,player):
        if player.current_room.name == "Laboratoire" and 'clé maître' not in player.inventory:
            return True
        return False
       

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()