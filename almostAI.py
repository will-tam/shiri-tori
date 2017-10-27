# -*- coding: utf-8 -*-

# Standard library import.
import random as rnd

# Project library import.
import sqlmanage


class Almost_AI():
    """
    (Not yet really) AI for this game to the single player's game.

    # Public attributes.
        sqlmgt = instance of SQLManage.
    """

    # Private attributes.


    # Public attributes.


    # Private methods.


    # Public methods.

    def __init__(self):
        """
        __init__ : initiate class
        @parameters : ...
        @return : none.
        """
        self.sqlmgt = sqlmanage.SQLManage()

    def choice(self):
        """
        The choice of the computer.
        !!!!!!! NO AI YET, just random choice !!!!!!
        @parameters : none.
        @return : the choosen computer word.
        """
        answers = ["ことば", "word"]
        return rnd.choice(answers)

######################

if __name__ == "__main__":
    print("Don't launch me directely, please !")
    print("Run python3 shiri-tory.py or directely if eXecution right(s) is/are ON.")
    sys.exit(1)
