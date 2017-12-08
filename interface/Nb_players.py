# -*- coding: utf-8 -*-

# Standard libraries import.
import sys

# Third libraries import.
import wx

# Projet modules import.


######################

class Nb_players():
    """
    Just Ask the number of player(s).
    Check no more than 5 included.
    0 means end of game.

    Public attributes.
        nb_players = save the number of players.
        quit = true if the player wants to leave, everelse false.
    """

    # Private attributes.


    # Public methods.

    def __init__(self):
        """
        __init__ : initiate class
        @parameters : ...
        @return : none.
        """
        self.nb_players = 0
        self.quit = false


    # Private methods.


def ask_number_of_players():
    """
    """

    return 0

######################

if __name__ == "__main__":
    print("Don't launch me directely, please !")
    print("Run python3 shiri-tory.py or directely shiri-tory.py if eXecution right(s) is/are ON.")
    sys.exit(1)
