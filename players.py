# -*- coding: utf-8 -*-

# Project library import.
import player

######################

class Players(player.Player):
    """
    Representing the whole declared players class.
    <Player> class daughter class.

    Public attributes :
        nickname = player nickname (PC).
        win_rounds = how many rounds a player wins (PC).
        loose_rounds = how many rounds a player losts (PC).
        turn = it's the player turn (True) or not (False) ? (PC)
        nb_players = number of players.
    """


    # Private attributes.


    # Public methods.
    def __init__(self):
        """
        __init__ : initiate class
        @parameters : nickname = a player nickname.
                      win_rounds = wan rounds number.
                      loose_rounds = lost rounds number.
                      turn = it's player turn (True), or not (False) ?
        @return : none.
        """
        self.Player.__init__()
        self.nb_players = 0

    def add_one_point_win(self):
        """
        Add 1 point to win points.
        @parameters : none.
        @return : none.
        """
        self.win_rounds += 1

    def add_one_point_lost(self):
        """
        Add 1 point to loose points.
        @parameters : none.
        @return : none.
        """
        self.loose_rounds += 1


    # Private methods.


if __name__ == "__main__":
    help(Players)
