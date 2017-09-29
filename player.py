# -*- coding: utf-8 -*-

class Player():
    """
    Representing only ONE player class.
    <Players> class parent class.

    Public attributes :
        nickname = player nickname.
        win_rounds = how many rounds a player wins.
        loose_rounds = how many rounds a player losts.
        turn = it's the player turn (True) or not (False) ?
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
        self.nickname = nickname
        self.win_rounds = 0
        self.loose_rounds = 0
        self.turn = False

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
    help(Player)
