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
         : dictionnary dictionnaries of players
            {p_id : {
                'nickname' : string,
                'won_rounds' : interger,
                'lost_rounds': interger,
                'turn' : boolean,
            }}
    """

    DIALOGS = {'nb_players_question_part_0' : "Nombre de joueurs entre 1 et 5 inclus",
               'nb_players_question_part_1' : "0 pour vous enfuire loin de moi. ",
               'nb_players_question_part_2' : "1 signifiant 2 joueurs, vous et ... moi. ",
               'nb_players_question_part_3' : "Pas plus de 5 joueurs.",
               'nb_players_question_part_4' : "Alors ?",
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
                                     'won_rounds' : 0,
                                     'lost_rounds' : 0,
                                     'turn' : False,}})

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

    def win_loose(self):
        """
        Winners and loosers players annoucement.
        @parameters : none.
        @return : a tuple of list (winners, loosers).
        """
        """
        all_nicknames_len = [len(self.game_engine.players.players[p_id]['nickname']) for p_id in self.game_engine.players.p_id]
        max_str_len = max(all_nicknames_len)
        """

        # Search the max of each points.
        max_win_points = max([self.players[p_id]['won_rounds'] for p_id in self.p_id])
        max_loose_points = max([self.players[p_id]['lost_rounds'] for p_id in self.p_id])

        # Pick up the name of each group according the max points of each group.
        winners = [self.players[p_id]['nickname'] for p_id in self.p_id if self.players[p_id]['won_rounds'] == max_win_points]
        loosers = [self.players[p_id]['nickname'] for p_id in self.p_id if self.players[p_id]['lost_rounds'] == max_loose_points]

        # Check if equality.
        old_pt = self.players[self.p_id[0]]['won_rounds']
        equality = True
        for p_id in self.p_id:
            if self.players[p_id]['won_rounds'] != old_pt:
                equality = False
                break
            old_pt = self.players[p_id]['won_rounds']

        if equality:
            loosers = None      # If all equality, so no looser. No ?

        return (winners, loosers)

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
            id = abs(hash((nickname, rnd.random())))
            if id not in self.p_id:
                unique = True

        return id


######################

if __name__ == "__main__":
    help(Players)
    print("Don't launch me directely, please !")
    print("Run python3 shiri-tory.py or directely shiri-tory.py if eXecution right(s) is/are ON.")
    sys.exit(1)
