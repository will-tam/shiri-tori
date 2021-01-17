# -*- coding: utf-8 -*-

# NOTE: uncomment to debug
print("{}.{}".format(__package__,__name__))

# Standard libraries import.
import sys

# Third libraries import.


# Projet modules import.
from . import Players, Rules, SQLManage, AI_like


######################

class Engine():
    """
    Main engine :
        - check components.
        - init components.
        - provides components.

    Public attributes.
        players, rules, sql, ai_like = instances of the corresponding components.
    """

    DIALOGS = {'no_want_play_bye' : "Peut-etre plus tard ?",
               'shuffle' : "Mélange des joueurs",
               'won_rounds' : "tours gagnés",
               'lost_rounds' : "tours perdus",
               'check_word' : "Vérification ... {} ...",
               'turn_lost' : "Désolé {}, vous perdez ce tour !",
               'turn_lost_1_pt' : "+1 point perdu pour vour, +1 point gagné pour les autres",
               'a_player_leave' : "{} voulais s'enfuire !!!",
               'ending_winner' : "Et {} :",
               'ending_looser' : "Donc, {} :",
               '1winner' : "le gagnant est",
               '1looser' : "le perdant est",
               'several_winners' : "les gagnants sont",
               'several_loosers' : "les perdants sont",
               'equality' : "Égalité !!!"}

    # Private attributes.


    # Public methods.

    def __init__(self):
        """
        __init__ : initiate class
        @parameters : none.
        @return : none.
        """
        self.sqlmanage = SQLManage.SQLManage()
        self.rules = Rules.Rules(self.sqlmanage)
        self.players = Players.Players()
        self.ai_like = AI_like.AI_like()

    # Properties
#    @property  # Getter
#    pass
#
#    @.setter #Setter
#    pass

    def win_loose_annouce(self, nb_winners, nb_loosers):
        """
        Winners and loosers players annoucement.
        @parameters : nb_winners = number of winners.
                      nb_loosers = number of loosers.
        @return : a tuple (winners annoucement, loosers annoucement).
        """
        w_annouce = self.DIALOGS['several_winners'] if nb_winners > 1 else self.DIALOGS['1winner']
        l_annouce = self.DIALOGS['several_loosers'] if nb_loosers > 1 else self.DIALOGS['1looser']

        return (w_annouce, l_annouce)


    # Private methods.


######################

if __name__ == "__main__":
    help(Engine)
    print("Don't launch me directely, please !")
    print("Run python3 shiri-tory.py or directely shiri-tory.py if eXecution right(s) is/are ON.")
    sys.exit(1)
