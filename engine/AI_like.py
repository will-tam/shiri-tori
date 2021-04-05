# -*- coding: utf-8 -*-

# NOTE: uncomment to debug
print("{}.{}".format(__package__,__name__))

# Standard libraries import.
import sys
import random as rnd
import time

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
               'my_turn' : "À mon tour",
               'i_loose' : "Et m... vous gagnez !",
               'i_loose_1_pt' : "+1 point gagné pour vous, +1 point perdu pour ... moi !",
               'i_win' : "Je gagne, vous perdez {}! ",
               'i_win_1_pt' : "+1 point gagné pour MOI, +1 point perdu pour ... VOUS !",
               'sly_bye' : "Forcément, vous avez senti que j'étais le plus fort !",}

    AI_PSEUDO = "The Best AI"

    # Private attributes.


    # Public methods.

    def __init__(self, sqlmanage):
        """
        __init__ : initiate class
        @parameters : sqlmanage = sqlmanage instance address.
        @return : none.
        """
        self.__sqlmanage = sqlmanage
        self.__nb_rows = self.__sqlmanage.number_of_row()

    def choice(self, first_hiragana=""):
        """
        The choice of the computer.
        !!!!!!! NO AI YET, just random choice !!!!!!
        @parameters : first_hiragana = 1st hiragana of the world shoud be choosen.
                                       Not an AI, but not so stupid.
        @return : the choosen computer word.
        """
        answer = "a"

        while answer[0] != first_hiragana:
            # Maybe one day, randrange() should be removed.
            rowid = rnd.randrange(1, self.__nb_rows + 1)
            #TODO : TypeError: 'NoneType' object is not subscriptable <--- WHY ?
            try:
                answer = self.__sqlmanage.what_at_rowid(rowid)
            except:
                answer = "a"
            if not first_hiragana:
                break

        return answer


    # Private methods.


######################

if __name__ == "__main__":
    help(AI_like)
    print("Don't launch me directely, please !")
    print("Run python3 shiri-tory.py or directely shiri-tory.py if eXecution right(s) is/are ON.")
    sys.exit(1)
