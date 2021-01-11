# -*- coding: utf-8 -*-

# NOTE: uncomment to debug
print("{}.{}".format(__package__,__name__))

# Standard libraries import.
import sys
import random as rnd

# Third libraries import.


# Projet modules import.


######################

class Players():
    """
    Keep a trace of an instantiated player.

    Public attributes.
        p_id : list of interger of unique players' id
        players : dictionnary dictionnaries of players
            {p_id :
                'name' : string.
                'score' : interger .
                'turn' : boolean.
                'answer' : string.
            }
    """

    DIALOGS = {'nb_players_question_0' : "Nombre de joueurs entre 0 et 5 inclus",
               'nb_players_question_1' : "0 pour vous enfuire loin de moi. ",
               'nb_players_question_2' : "1 signifiant 2 joueurs, vous et ... moi. ",
               'nb_players_question_3' : "Pas plus de 5 joueurs.",
               'nb_players_question_4' : "Alors ? >>>  ",
               'ask_nickname' : "Donnez-moi votre pseudo s'il vous plait.",
               'player_name_turn' : "Joueur {}, à vous.", }

    # Private attributes.


    # Public methods.

    def __init__(self):
        """
        __init__ : initiate class
        @parameters : none.
        @return : none.
        """
        self.p_id = []
        self.players = {}

    def add(self, name):
        """
        Add a player.
        @parameters : name = name of the player.
        @return : none.
        """
        # Trouver player_id unique
        # Ajout de player_id dans liste des p_id
        # Ajout dans players d'un dico {p_id : {'name' : name, 'score' : 0, 'turn' : False, 'answer' : ""}}
        pass

    def shuffle(self):
        """
        Mix 10 times (why not) the p_id list in place.
        @parameters : none.
        @return : none.
        """
        print(self.p_id)
        for i in range(0, 10):
            rnd.shuffle(self.p_id)
        print(self.p_id)

    # Private methods.

    def __find_unique_id(self):
        """
        Find an unique id for a player.
        @parameters : none.
        @return : id found.
        """
        unique = False
        id = 0

        while not unique:
            # Trouver l'id qui va bien

            if id not in self.p_id:
                unique = True

        return id

######################

if __name__ == "__main__":
    help(Players)
    print("Don't launch me directely, please !")
    print("Run python3 shiri-tory.py or directely shiri-tory.py if eXecution right(s) is/are ON.")
    sys.exit(1)
