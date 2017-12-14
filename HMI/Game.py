# -*- coding: utf-8 -*-

# Standard libraries import.
import sys

# Third libraries import.
import wx

# Projet modules import.
import player
import one_game
import almostAI

######################

class Game():
    """
    wx.Frame class derivated class.

    Ask the nickname of each players, according their number.

    Public attributes.
    """

    # Private attributes.


    # Public methods.

    def __init__(self, parent, playersI, nb_players):
        """
        __init__ : initiate class
        @parameters : playersI = instance of players.
                      nb_players = number of players.
        @return : none.
        """
        pass


    # Private methods.

######################

def ze_GAME(wx_app, playersI, nb_players):
    """
    Entry point of the HMI.
    @parameters : wx_app = the wx application instance.
                  playersI = instance of players.
                  nb_players = number of players who asking the nickname.
    @return : who stop the game.
    """
    game_hmi = Game(None, playersI, nb_players)
    game_hmi.Show()

    wx_app.MainLoop()

    return "Him/her"

######################

if __name__ == "__main__":
    print("Don't launch me directely, please !")
    print("Run python3 shiri-tory.py or directely shiri-tory.py if eXecution right(s) is/are ON.")
    sys.exit(1)
