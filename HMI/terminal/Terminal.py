#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Standard library import.
import sys

# Third-part library import.

# Project library import.

######################

class Terminal():
    """
    Class to manage terminal part of shiri-tori.

    Public attributes.
        game_engine = instances of the game engine.
    """

    EOL = "\n"

    def __init__(self, game_engine):
        """
        __init__ : initiate class
        @parameters : game_engine = engine instance address.
        @return : none.
        """
        self.game_engine = game_engine

    def ask_number_of_players(self):
        """
        Just Ask the number of player(s).
        Check no more than 5 included.
        0 means end of game.
        @parameters : none.
        @return : the answer.
        """
        dialog_question_keys = ['nb_players_question_0',
                                'nb_players_question_1',
                                'nb_players_question_2',
                                'nb_players_question_3',
                                'nb_players_question_4']

        dialog_question = [self.game_engine.players.DIALOGS[dqk] for dqk in dialog_question_keys]

        question = self.EOL
        question += self.EOL.join(dialog_question)

        nb_players = 6  # We directely enter inside next loop.

        while nb_players > 5:
            try:
                nb_players = int(input(question))   # Only int expected.
            except:
                print("\n\tDésolé, mais j'aimerais un nombre seulement.\n")

        return nb_players

    def main(self):
        """
        Main function of the terminal IHM.
        @parameters : none.
        @return : 0 = all was good.
        """
        # NOTE : retirer le # suivant, après mise au point.
    #    print("\x1b[2J\x1b[;H")

        nb_players = self.ask_number_of_players()

        if nb_players == 0:
            print("{0}{1}{0}".format(self.EOL, self.game_engine.DIALOGS['no_want_play_bye']))
            return 0

        """

        playersI = ask_nickname(nb_players)

        nickname_away = main_loop(playersI, nb_players)

        if nickname_away:
            if nb_players == 1:
                print("{}Of course, you have feel i was the strongest !\n".format(5 * "\n"))

            else:
                print("{}{} would to get away !!!\n".format(5 * "\n", nickname_away))

        display_points(playersI)
        """
        return 0

######################

if __name__ == "__main__":
    help(Terminal)
    print("Don't launch me directely, please !")
    print("Run python3 shiri-tory.py or directely shiri-tory.py if eXecution right(s) is/are ON.")
    sys.exit(1)
