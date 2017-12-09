#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Standard library import.
import sys
import wx

# Third-part library import.

# Project library import.
import HMI.Nb_players as HMI_Nb_players

######################

def graphical_mode():
    """
    Main for interface mode.
    @parameters : none.
    @return : 0 = all was good.
    """

    nb_players = HMI_Nb_players.ask_number_of_players()

    print("nb_players =", nb_players)

    return 0

######################

if __name__ == "__main__":
    print("Don't launch me directely, please !")
    print("Run python3 shiri-tory.py or directely shiri-tory.py if eXecution right(s) is/are ON.")
    sys.exit(1)
