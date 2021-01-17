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
    WAIT_ASK = " >>> "

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
        question += self.WAIT_ASK

        nb_players = 6  # We directely enter inside next loop.

        while nb_players > 5:
            try:
                nb_players = int(input(question))   # Only int expected.
            except:
                print("\n\tDésolé, mais j'aimerais un nombre seulement.\n")

        return nb_players

    def ask_nickname(self, nb_players):
        """
        Just ask the nickname of each player.
        If there is only one, a second one is adding, the computer it-self.
        @parameters : nb_players = number of player(s).
        @return : the nicknames.
        """
        nicknames = []

        if nb_players == 1:
            print("{0}{1}{0}".format(self.EOL, self.game_engine.ai_like.DIALOGS['just_us']))
            nicknames.append(input(self.game_engine.players.DIALOGS['ask_nickname'] + self.WAIT_ASK))
            # Manage the unknown player in single player mode.
            if nicknames[0] == "":
                nicknames[0] = self.game_engine.players.find_me_a_nickname(0)
            nicknames.append("The Best IA")     # For 1 player mode, also computer plays.
        else:
            for i in range(1, nb_players + 1):
                unique_name = False
                while not unique_name:
                    nn = input(self.game_engine.players.DIALOGS['ask_nickname_multi'].format(i)  + self.WAIT_ASK)
                    # Manage the unknown player in several players mode.
                    if nn == "":
                        nn = self.game_engine.players.find_me_a_nickname(i)
                    if nn in nicknames:
                        print(self.game_engine.players.DIALOGS['already_choosen'].format(nn) + " ", end='')
                    else:
                        unique_name = True
                nicknames.append(nn)

        return nicknames

    def display_points(self):
        """
        Display the win and loose points as a table
        @parameters : none.
        @return : none.
        """
        won_string = self.game_engine.DIALOGS['won_rounds']
        lost_string = self.game_engine.DIALOGS['lost_rounds']
        won_string_len = len(won_string)
        lost_string_len = len(lost_string)

        # Take the length of the longest nicknames.
        all_nicknames_len = [len(self.game_engine.players.players[p_id]['nickname']) for p_id in self.game_engine.players.p_id]
        max_str_len = max(all_nicknames_len)

        # Add the lenth of the 2 strings won_string and lost_string.
        width = max_str_len + won_string_len + lost_string_len

        # Add the border, beetween the 2 strings, beetween nickname and the table body.
        width += 10

        print(width * "*")
        print("* {} * {} * {} *".format(max_str_len * " ", won_string, lost_string))

        for p_id in self.game_engine.players.p_id:
            nickname = self.game_engine.players.players[p_id]['nickname']
            won_rounds = self.game_engine.players.players[p_id]['won_rounds']
            lost_rounds = self.game_engine.players.players[p_id]['lost_rounds']

            pfs = max_str_len - len(nickname)    # Number of white spaces after the nickname.
            wfs = won_string_len - len(str(won_rounds))  # After the won points.
            plr = lost_string_len - len(str(lost_rounds))   # At last the lost points.
            print("* {pn}{pfs} * {pwr}{wfs} * {plr}{lfs} *".format(pn = nickname,
                                                                   pfs = pfs * " ",
                                                                   pwr = won_rounds,
                                                                   wfs = wfs * " ",
                                                                   plr = lost_rounds,
                                                                   lfs = plr * " "))

        print(width * "*", self.EOL)

        # Annoucement,with grammatical correction, according find winners and loosers players.
        winners, loosers = self.game_engine.players.win_loose()
        winners_str, loosers_str = self.game_engine.win_loose_annouce(len(winners), len(loosers))

        print(self.game_engine.DIALOGS['ending_winner'].format(winners_str))
        for winner in winners:
            print("\t{}".format(winner))

        print(self.game_engine.DIALOGS['ending_looser'].format(loosers_str))
        for looser in loosers:
            print("\t{}".format(looser))

        print(self.EOL)

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

        self.game_engine.players.register_players(self.ask_nickname(nb_players))

        print("{0}{1}{0}".format(self.EOL, self.game_engine.DIALOGS['shuffle']))
        self.game_engine.players.shuffle()

        """
        nickname_away = main_loop(playersI, nb_players)

        if nickname_away:
            if nb_players == 1:
                print("{}Of course, you have feel i was the strongest !\n".format(5 * "\n"))

            else:
                print("{}{} would to get away !!!\n".format(5 * "\n", nickname_away))
        """

        self.display_points()


        return 0

######################

if __name__ == "__main__":
    help(Terminal)
    print("Don't launch me directely, please !")
    print("Run python3 shiri-tory.py or directely shiri-tory.py if eXecution right(s) is/are ON.")
    sys.exit(1)
