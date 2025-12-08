# Description: The actions module.

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.


# The error message is stored in the MSG0 and MSG1 variables and formatted with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

class Actions:

    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction (N, E, S, O) + (U,D).

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> go(game, ["go", "N"], 1)
        True
        >>> go(game, ["go", "N", "E"], 1)
        False
        >>> go(game, ["go"], 1)
        False

        """
        
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the direction from the list of words.
        direction = list_of_words[1]
        # Move the player in the direction specified by the parameter.
        S = ["N","Nord","NORD","n","nord","S","Sud","sud","SUD","s","O","Ouest","OUEST","ouest","o","E","Est","EST","e","est","U","Up","UP","u","up","D","DOWN","d","down","Down" ]
        if (list_of_words[1] not in S):
            print("La commande n'existe pas.")

        elif (direction in ("N","Nord","NORD","n","nord")):
            player.move("N")
        elif (direction in ("S","Sud","sud","SUD","s")):
            player.move("S")
        elif (direction in ("O","Ouest","OUEST","ouest","o")):
            player.move("O")
        elif (direction in ("E","Est","EST","e","est")):
            player.move("E")
        elif (direction in ("U","Up","UP","u","up")):
            player.move("U")
        elif (direction in ("D","DOWN","d","down","Down")):
            player.move("D")

        return True

    def back(game, list_of_words, number_of_parameters):
        """
        Go back to the previous room.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.
        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        player = game.player
        previous_room_name = player.go_back()
        
        if previous_room_name is None:
            print("\nVous êtes à la première pièce, impossible de revenir en arrière !\n")
            return False
        
        # Trouver la pièce précédente dans la liste des salles
        for room in game.rooms:
            if room.name == previous_room_name:
                player.current_room = room
                print(player.get_history_string())
                print(player.current_room.get_long_description())
                return True
        
        return False

    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False

        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci {player.name} d'avoir participé à cet escape game gratuit, bien joué et à bientôt !! .\n"
        print(msg)
        game.finished = True
        return True

    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True
    
    def show_inventory(game, words, nb):
        inventory = game.player.inventory

        print("\nVotre inventaire :")

        if not inventory:
            print("  (vide)")
        else:
            for obj in inventory:
                print(f"  - {obj}")

    def add_to_inventory(game, item):
        game.player.inventory.append(item)
        print(f"\n📦 Vous obtenez : {item}")

    

    def enigme_maths(game):

        # Ici tu choisis ton énigme :
        enigme = "Le double de l'âge du manoir moins le nombre de pièce au cube" 

        reponse_attendue = "76"

        print("\nÉnigme :")
        print(enigme)

        # Pose la question au joueur :
        reponse = input("\nVotre réponse : ").lower().strip()

        if reponse == reponse_attendue:
            print("\n🎉 Une des pierres ressort du mur et qui se casse en tombant, à l'intérieur, il se trouve une carte ' 2 de carreau '.")
            Actions.add_to_inventory(game, "2 de carreau")
            return True
        else:
            print("\n❌ Il ne s'est rien passé.")
            return False
        
    def enigme_sonore(game):

        reponse_attendue = "re mi do fa sol"

        # Pose la question au joueur :
        reponse = input("\n🎵🎵🎵Votre réponse (en miniscule avec les espaces): ").lower().strip()

        if reponse == reponse_attendue:
            print("\n🎉 L'enceinte du piano s'ouvre, à l'intérieur se trouve la carte ' 8 de trèfle '.")
            Actions.add_to_inventory(game, "8 de trèfle")
            return True
        else:
            print("\n❌ Il ne s'est rien passé.")
            return False

    def inspect(game, words, nb):
        if len(words) < 2:
            print("Inspecter quoi ?")
            return

        objet = words[1].lower()
        current_room = game.player.current_room

        # Si l'objet est interactif dans cette pièce
        if objet in current_room.interactions:
            current_room.interactions[objet](game)   # Appelle la fonction associée
        else:
            print("Vous ne voyez rien de spécial concernant cela.")


    def inspecter_grimoire(game):
        print("\nVous ouvrez le vieux grimoire poussiéreux...")

        texte = (
        "Les pages sont jaunies, mais un symbole étrange attire votre attention.\n"
        "Au bas d'une page, vous lisez un chiffre entouré de glyphes :\n\n"
        "    → 0919\n\n"
        "Ce code semble important... peut-être ouvrira-t-il un coffre ailleurs dans le manoir."
        )

        print(texte)

    def inspecter_doudou(game):
        texte = (
        "Peut être qu'un doudou pourrait plaire à un enfant......"
        )
        print(texte)
        Actions.add_to_inventory(game, "un doudou")

    def inspecter_ps5(game):
        texte = (
        "Peut être qu'un ps5 pourrait plaire à un enfant......"
        )
        print(texte)
        Actions.add_to_inventory(game, "un ps5")


    def ouvre_coffre(game):

        # Ici tu choisis ton énigme :
        indice = "Le coffre étant fermé, il faut un code pour l'ouvrir..." 

        reponse_attendue = "0919"

        print("\nIndice :")
        print(indice)

        # Pose la question au joueur :
        reponse = input("\nVotre réponse : ").lower().strip()

        if reponse == reponse_attendue:
            print("\n🎉 Le coffre s'ouvre, il se trouve une carte ' roi de cœur ' et une loupe.")
            Actions.add_to_inventory(game, "roi de cœur")
            Actions.add_to_inventory(game, "une loupe")
            return True
        else:
            print("\n❌ Le code n'est pas bon, le coffre reste bloqué.")
            return False
        
    def femme(game):
        print("\nLa femme vous regarde mystérieusement...")

        inventory = game.player.inventory

        bijou = "bijou ancien"
        carte_donnee = "as de pique"

        # Vérifier si le joueur a déjà la carte
        if carte_donnee in inventory:
            print("Elle sourit : « Nous avons déjà échangé, n'est-ce pas ? »")
            return

        # Vérifier si le joueur possède le bijou
        if bijou in inventory:
            print("\n« Oh ! Ce bijou... je le reconnaîtrais entre mille ! »")
            print("\nElle vous tend une carte en échange : L'as de pique !")

            inventory.remove(bijou)  # Il donne le bijou
            print("Vous recevez : As de pique.")

            Actions.add_to_inventory(game,carte_donnee)  # Elle donne la carte
        else:
            print("Elle secoue la tête : « Je n’ai rien pour vous tant que vous ne m'apportez pas quelque chose de précieux… »")
    

    def inspecter_enfant(game):
        print("\nL'enfant vous jette un regard noir....")

        inventory = game.player.inventory

        doudou_donne = "un doudou"
        bijou = "bijou ancien"

        # Vérifier si le joueur a deja le bijou
        if bijou in inventory:
            print("\nL'enfant rigole en disant : « Vous me prenez pour une source infinie ? »")
            return

        # Vérifier si le joueur possède le doudou
        if doudou_donne in inventory:
            print("« Oooh ! Mon jouet préféré !! »")
            print("Il échange le doudou contre le bijou")

            game.player.inventory.remove(doudou_donne)  # on lui donne le doudou
            print("Vous recevez : Un bijou ancien.")

            Actions.add_to_inventory(game, bijou)  # Il donne le bijou
        else:
            print("Enfant retourne se coucher dans le lit.")



    def inspecter_tableau(game):
        print("\nVous vous approchez du tableau poussiéreux...")

        inventory = game.player.inventory

    # Vérifier les lunettes
        if "une loupe" in inventory:
            print("Grâce à votre loupe, vous parvenez à déchiffrer une phrase minuscule :")
            print("\n   « Réveille mon Mii qui dort face au sol. »")
            print("\nCette phrase pourrait être importante ailleurs...")
        else:
            print("La phrase semble écrite très petit... impossible de lire quoi que ce soit.")


    def inspecter_piano(game):
        print("\nVous ouvrez le couvercle du piano...")

        # On lance l’énigme sonore
        résultat = Actions.enigme_sonore(game)

        if résultat:
            print("YEAH !")
        else:
            print("Le mécanisme ne semble pas réagir.")

    def coffre_clé(game):
        print("\nCeci est un coffre maître, il est indiqué de gauche à droit les couleurs suivantes :")
        print("\ncœur, pique, carreau, trèfle")

        reponse_attendue = "roi as 2 8"

        # Pose la question au joueur :
        reponse = input("\nVotre réponse (en miniscule avec les espaces): ").lower().strip()

        if reponse == reponse_attendue:
            print("\n🎉Bien joué ! Vous arrivez bientôt à la fin !")
            Actions.add_to_inventory(game, "clé maître")
            return True
        else:
            print("\n❌ Le coffre reste bloqué...")
            return False
    
    def ouvre_porte(game):

        inventory = game.player.inventory
        clé = 'clé maître'

        # Vérifier si le joueur a la clé maître
        if clé in inventory:
            print(f"\n🎉 Félicitation {game.player.name} ! Vous avez réussi ! La porte s'ouvre lentement....Vous êtes maintenant en liberté ! Vive le python 🐍")
            return
        else:
            print("Il vous manque un objet précis pour sortir de ce manoir hanté.....va chercher ailleurs 👻 ")

    def history(game, list_of_words, number_of_parameters):
        """
        Display the list of all visited rooms.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.
        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Get the history of visited rooms from the player
        visited_rooms = game.player.get_history()
        
        print("\nPièces visitées :")
        if not visited_rooms:
            print("  Aucune pièce visitée pour le moment.")
        else:
            for i, room in enumerate(visited_rooms, 1):
                print(f"  {i}. {room}")
        print()
        return True



