# Description: Game class

# Import modules

from room_projet import Room
from player_projet import Player
from command_projet import Command
from actions_projet import Actions


class Game:
    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
 
   

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
        inventory = Command("inventory", " : afficher l'inventaire", Actions.show_inventory, 0)
        self.commands["inventory"] = inventory


        # Setup rooms

        Hall = Room("Hall", "actuellement dans le Hall, une lettre est posée sur la table écrivant 'Boooooh 👻👻👻, vous êtes dans un manoir hanté qui a été fondé en 1879. Si vous ne sortez pas par la porte de sortie qui se trouve quelque part dans ce manoir à temps, vous resterez prisonnier à jamais....... Je vous souhaite bon courage !'")
        self.rooms.append(Hall)
        Salon = Room("Salon", "dans le Salon, plongé dans une pénombre frissonnante, était rempli de meubles anciens recouverts de draps poussiéreux. On constate la présence d'une femme.")
        self.rooms.append(Salon)
        Bibliothèque = Room("Bibliothèque", "dans la Bibliothèque, saturée d'un parfum de vieux parchemin, alignait ses étagères grinçantes dans une obscurité inquiétante. On observe un grimoire et un doudou au sol, et un mur gravé d'un langage ancien.")
        self.rooms.append(Bibliothèque)
        Chambre = Room("Chambre", "dans la Chambre, figée dans une lueur blafarde, dévoilait un lit et des rideaux immobiles, sous le lit, il se trouve un coffre vérrouillé, et un enfant assis sur ce dernier.")
        self.rooms.append(Chambre)
        Salle_de_musique = Room("Salle_de_musique", "dans la Salle de musique, résonnait d'un silence oppressant, où un piano délaissé semblait attendre que les mains invisibles rejouent une mélodie oubliée, à coté du piano, il se trouve une ps5.")
        self.rooms.append(Salle_de_musique)
        Bureau = Room("Bureau", "dans le Bureau, encombré de papiers jaunis et d'un large secrétaire craquant, baignait dans une atmosphère lourde, il y a un tableau poussiéreux sur le mur, un coffre doré sur une table dans un coin et une porte mystérieuse en face de vous....")
        self.rooms.append(Bureau)

        Bibliothèque.interactions = {"mur": Actions.enigme_maths,
                                    "grimoire": Actions.inspecter_grimoire,
                                    "doudou": Actions.inspecter_doudou}

        Bureau.interactions = {"tableau": Actions.inspecter_tableau,
                               "coffre" : Actions.coffre_clé,
                               "porte": Actions.ouvre_porte}

        Chambre.interactions = {"coffre": Actions.ouvre_coffre,
                                "enfant": Actions.inspecter_enfant}

        Salle_de_musique.interactions = {"ps5": Actions.inspecter_ps5,
                                        "piano": Actions.inspecter_piano}

        Salon.interactions = {"femme": Actions.femme}


        # Create exits for rooms

        Hall.exits = {"N" : Chambre, "E" : Salon, "S" : None, "O" : Bureau}
        Salon.exits = {"N" : Bibliothèque, "E" : None, "S" : None, "O" : Hall}
        Bibliothèque.exits = {"N" : None, "E" : None, "S" : Salon, "O" : Chambre}
        Chambre.exits = {"N" : None, "E" : Bibliothèque, "S" : Hall, "O" : Salle_de_musique}
        Salle_de_musique.exits = {"N" : None, "E" : Chambre, "S" : Bureau, "O" : None}
        Bureau.exits = {"N" : Salle_de_musique, "E" : Hall, "S" : None, "O" : None}

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
        print(f"\nBienvenue {self.player.name} dans Alice In Borderland !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()