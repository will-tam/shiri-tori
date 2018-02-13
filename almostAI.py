# -*- coding: utf-8 -*-

# Standard library import.
import sys
import random as rnd
import time

# Project library import.
import sqlmanage


class Almost_AI():
    """
    (Not yet really) AI for this game to the single player's game.

    # Public attributes.
        sqlmgt = instance of SQLManage.
    """

    # Private attributes.
    # __nb_rows = number of rows in the table.


    # Private methods.


    # Public methods.

    def __init__(self):
        """
        __init__ : initiate class.
        @parameters : none.
        @return : none.
        """
        self.sqlmgt = sqlmanage.SQLManage()
        self.__nb_rows = self.sqlmgt.number_of_row()

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
                answer = self.sqlmgt.what_at_rowid(rowid)
            except:
                answer = "a"
            if not first_hiragana:
                break

        return answer

    def HMI_turn(self, game_hmi, p_answer):
        """
        Update the player number who it's the turn.
        @parameters : game_hmi = the hmi game instance.
                      p_answer = previous player's answer.
        @result : none.
        """
        p_answer = self.choice(p_answer[-1]) if p_answer else self.choice()

        game_hmi.player_answer.SetValue(p_answer)
        # Need both of them to appear in game_hmi.player_answer !!!
        game_hmi.player_answer.Refresh()
        game_hmi.player_answer.Update()

        time.sleep(5)

        game_hmi.press_btn_validate()

######################

if __name__ == "__main__":
    print("Don't launch me directely, please !")
    print("Run python3 shiri-tory.py or directely if eXecution right(s) is/are ON.")
    sys.exit(1)
