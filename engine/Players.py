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
            {p_id : {
                'nickname' : string,
                'score' : interger,
                'turn' : boolean,
                'answer' : string,
            }}
    """

    DIALOGS = {'nb_players_question_0' : "Nombre de joueurs entre 0 et 5 inclus",
               'nb_players_question_1' : "0 pour vous enfuire loin de moi. ",
               'nb_players_question_2' : "1 signifiant 2 joueurs, vous et ... moi. ",
               'nb_players_question_3' : "Pas plus de 5 joueurs.",
               'nb_players_question_4' : "Alors ?",
               'ask_nickname' : "Donnez-moi votre pseudo s'il vous plait.",
               'ask_nickname_multi' : "Joueur {}, votre pseudo s'il vous plait.",
               'player_name_turn' : "Joueur {}, à vous.",
               'noname_1_player' : "Vous, l'inconnu(e)",
               'noname_X_players' : "L'inconnu(e) {}",
               'already_choosen' : "{} est déjà pris !", }

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

    def register_players(self, nicknames):
        """
        Add a players in players dictionnary.
        @parameters : nicknames = list of players nicknames.
        @return : none.
        """
        for nickname in nicknames:
            p_id = self.__find_unique_id(nickname)
            self.p_id.append(p_id)
            self.players.update({p_id :
                                    {'nickname' : nickname,
                                     'score' : 0,
                                     'turn' : False,
                                     'answer': ""}})

    def shuffle(self):
        """
        Mix 10 times (why not) the p_id list in place.
        @parameters : none.
        @return : none.
        """
        for i in range(0, 10):
            rnd.shuffle(self.p_id)

    def find_me_a_nickname(self, player_num):
        """
        Return something as "unknown" to an empty player's nickname.
        @parameters : player_num = number of player who find a name.
        @return : see self.DIALOGS, with a digit if several.
        """
        ze_best_nn = self.DIALOGS['noname_1_player'] if player_num == 0 else self.DIALOGS['noname_X_players'].format(player_num)
        return ze_best_nn

    # Private methods.

    def __find_unique_id(self, nickname):
        """
        Find an unique id for a player.
        @parameters : nickname = create player id from this nickname.
        @return : unique player id found.
        """
        unique = False

        while not unique:
            # Using of Python hash function to find a hash. A random is add in the hash function
            # to hoe to be sure the player id will be unique at first time.
            # while loop is to add one more (useless ?) security.
            id = hash((nickname, rnd.random()))
            if id not in self.p_id:
                unique = True

        return id


######################

if __name__ == "__main__":
    help(Players)
    print("Don't launch me directely, please !")
    print("Run python3 shiri-tory.py or directely shiri-tory.py if eXecution right(s) is/are ON.")
    sys.exit(1)
