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
        players, rules, sql, ia_like = instances of the corresponding components.
    """

    DIALOGS = {'no_want_play_bye' : "Peut-etre plus tard ?",
               'check_word' : "Vérification ... {} ...",
               'loose_turn' : "Désolé {}, vous perdez ce tour !",
               'losse_turn_1_pt' : "+1 point perdu pour vour, +1 point gagné pour les autres",
               'a_player_leave' : "{} voulais s'enfuire !!!",}

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

    # Private methods.


######################

if __name__ == "__main__":
    help(Engine)
    print("Don't launch me directely, please !")
    print("Run python3 shiri-tory.py or directely shiri-tory.py if eXecution right(s) is/are ON.")
    sys.exit(1)
