# -*- coding: utf-8 -*-

# NOTE: uncomment to debug
print("{}.{}".format(__package__,__name__))

# Standard libraries import.
import sys


# Third libraries import.


# Projet modules import.


######################

class AI_like():
    """
    Special player : the computer.
    Always plays if there is only 1 player.
    If more than 1 player, ask if it could play.

    Public attributes.
    """

    DIALOGS = {'just_us' : "Ok, c'est juste entre vous et moi !",
               'my_turn' : "My turn",
               'i_loose' : "Et m... vous gagnez {} !",
               'i_loose_1_pt' : "+1 point gagné pour vous, +1 point perdu pour ... moi !",
               'i_win' : "Je gagne, vous perdez {}! ",
               'i_win_1_pt' : "+1 point gagné pour MOI, +1 point perdu pour ... VOUS !",
               'sly_bye' : "Forcément, vous avez senti que j'étais le plus fort !",}

    AI_PSEUDO = "The Best AI"

    # Private attributes.


    # Public methods.

    def __init__(self):
        """
        __init__ : initiate class
        @parameters : none.
        @return : none.
        """
        pass


    # Private methods.


######################

if __name__ == "__main__":
    help(AI_like)
    print("Don't launch me directely, please !")
    print("Run python3 shiri-tory.py or directely shiri-tory.py if eXecution right(s) is/are ON.")
    sys.exit(1)
