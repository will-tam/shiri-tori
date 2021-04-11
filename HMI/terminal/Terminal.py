#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Standard library import.
import sys

# Third-part library import.

# Project library import.
from ..engine import Engine

######################

class Terminal(Engine.Engine):
    """
    Class to manage terminal part of shiri-tori.

    Public attributes.
    """

    EOL = "\n"
    TAB = "\t"
    WAIT_ASK = " >>> "

    def __init__(self):
        """
        __init__ : initiate class
        @parameters : none.
        @return : none.
        """
        super().__init__()

    def ask_number_of_players(self):
        """
        Just Ask the number of player(s).
        Check no more than 5 included.
        0 means end of game.
        @parameters : none.
        @return : the answer.
        """
        super().ask_number_of_players()     # init _dialog_question from parent class ask_number_of_players()

        question = self.EOL
        question += self.EOL.join(self._dialog_question)
        question += self.WAIT_ASK

        nb_players = 6  # We directely enter inside next loop.

        while nb_players > 5:
            try:
                nb_players = int(input(question))   # Only int expected.
            except:
                print("{0}{1}{2}{0}".format(self.EOL, self.TAB, self.DIALOGS['only_number']))

        return nb_players

    def ask_nickname(self, nb_human_players):
        """
        Just ask the nickname of each player.
        If there is only one, a second one is adding, the computer it-self.
        @parameters : nb_human_players = number of human player(s).
        @return : the nicknames.
        """
        super().ask_nickname()

        if nb_human_players == 1:
            print("{0}{1}{0}".format(self.EOL, self.ai_like.DIALOGS['just_us']))

            unique_name = False
            while not unique_name:
                nn = input(self.players.DIALOGS['ask_nickname'] + self.WAIT_ASK)

                # Manage the unknown player in single player mode.
                if nn == "":
                    nn = self.players.find_me_a_nickname(0)

                if nn in self._nicknames:
                            print(self.players.DIALOGS['already_choosen'].format(nn) + " ", end='')

                else:
                    unique_name = True

            self._nicknames.append(nn)
            self._nicknames.append(self.ai_like.AI_PSEUDO)     # For 1 player mode, also computer plays.

        else:
            for i in range(1, nb_human_players + 1):      # this i index will be used in next code.

                unique_name = False
                while not unique_name:
                    nn = input(self.players.DIALOGS['ask_nickname_multi'].format(i)  + self.WAIT_ASK)

                    # Manage the unknown player in several players mode.
                    if nn == "":
                        nn = self.players.find_me_a_nickname(i)

                    if nn in self._nicknames:
                        print(self.players.DIALOGS['already_choosen'].format(nn) + " ", end='')

                    else:
                        unique_name = True

                self._nicknames.append(nn)

        return self._nicknames

    def main_loop(self, nb_human_players):
        """
        The game main loop.
        @parameters : nb_human_players = number of human players.
        @return : name of the player who gets away.
        """
        super().main_loop()

        # THE main loop itconsole_mode.py-self.
        now_player = iter(self.players.p_id)

        first_answer = True

        while self.p_answer != "0":
            try:
                p_id = next(now_player)

                nickname = self.players.players[p_id]["nickname"]
                # NOTE: uncomment to debug
#                print(nb_human_players)
#                print(p_id)

                if nb_human_players == 1 and nickname == self.ai_like.AI_PSEUDO:     # Only 1 player, and it's computer's turn.
                    self.p_answer = self.ai_like.choice(self.p_answer[-1]) if self.p_answer else self.ai_like.choice()
                    print("{} >>> {}".format(self.ai_like.DIALOGS['my_turn'], self.p_answer))
                else:   # everelse it's player turn (it runs for 1 or several human players).
                    print("{}, {} >>>".format(nickname, self.DIALOGS['your_turn']), end='')
                    repeat_question = True
                    if repeat_question:
                        try:
                            self.p_answer = input(" ")
                            repeat_question = False
                        except UnicodeDecodeError:
                            repeat_question = True
                    if self.p_answer == "0":         # 0 means exit game.
                        return nickname

                print("{} ... {} ...".format(self.DIALOGS['check_word'], self.p_answer), end="")

                checked_answer = self.rules.check_answer(self.p_answer, first_answer)
                print(checked_answer[1])

                if not checked_answer[0]:     # bad answer !
                    if nb_human_players == 1 and nickname == self.ai_like.AI_PSEUDO:         # Only 1 player and it's the computer's turn.
                        to_diag = "{}{}".format(self.TAB, self.ai_like.DIALOGS['i_loose'])
                        to_diag += "{0}{1}{2}{0}".format(self.EOL, self.TAB, self.ai_like.DIALOGS['i_loose_1_pt'])

                    elif nb_human_players == 1 and nickname != self.ai_like.AI_PSEUDO:       # Only 1 player and it's the human's turn.
                        to_diag = self.TAB
                        to_diag += self.ai_like.DIALOGS['i_win'].format(nickname)
                        to_diag += "{0}{1}{2}{0}".format(self.EOL, self.TAB, self.ai_like.DIALOGS['i_win_1_pt'])

                    else:       # Several human players.
                        to_diag = self.TAB
                        to_diag += self.DIALOGS['turn_lost'].format(nickname)

                        to_diag += "{2}{0}{1}{2}".format(self.TAB, self.DIALOGS['turn_lost_1_pt'], self.EOL)

                    print(to_diag)

                    # Update win and loose points for each players.
                    for player_id in self.players.players.keys():
                        if player_id == p_id:
                            self.players.players[player_id]['lost_rounds'] += 1
                        else:
                            self.players.players[player_id]['won_rounds'] += 1
                    self.p_answer = ""      # As it was a bad answer, avoid to enter in infinite loop in Almost_AI.choice()
                    first_answer = True
                else:
                    first_answer = False    # The players are playing.
                    print("\n")

                # NOTE: uncomment to debug
    #            self.p_answer = "0"

                print("")

            except StopIteration:
                now_player = iter(self.players.p_id)

    def display_points(self):
        """
        Display the win and loose points as a table
        @parameters : none.
        @return : none.
        """
        super().display_points()

        won_string_len = len(self._won_string)
        lost_string_len = len(self._lost_string)

        # Take the length of the longest nicknames.
        all_nicknames_len = [len(self.players.players[p_id]['nickname']) for p_id in self.players.p_id]
        max_str_len = max(all_nicknames_len)

        # Add the lenth of the 2 strings won_string and lost_string.
        width = max_str_len + won_string_len + lost_string_len

        # Add the border, beetween the 2 strings, beetween nickname and the table body.
        width += 10

        print(width * "*")
        print("* {} * {} * {} *".format(max_str_len * " ", self._won_string, self._lost_string))

        for player in self.players.players.values():
            nickname = player['nickname']
            won_rounds = player['won_rounds']
            lost_rounds = player['lost_rounds']

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
        winners, loosers = self.players.win_loose()
        if not loosers:
            print(self.DIALOGS['equality'])

        else:
            winners_str, loosers_str = self.win_loose_annouce(len(winners), len(loosers))

            print(self.DIALOGS['ending_winner'].format(winners_str))
            for winner in winners:
                print("\t{}".format(winner))

            print(self.DIALOGS['ending_looser'].format(loosers_str))
            for looser in loosers:
                print("\t{}".format(looser))

        print(self.EOL)

    def main(self):
        """
        Main function of the terminal IHM.
        @parameters : none.
        @return : 0 = all was good.
        """
        print("\x1b[2J\x1b[;H")

        # How many players want to play.
        nb_human_players = self.ask_number_of_players()

        # Actually, nobody wants to play T_T !
        if nb_human_players == 0:
            print("{0}{1}{0}".format(self.EOL, self.DIALOGS['no_want_play_bye']))
            return 0

        # Register all players.
        self.players.register_players(self.ask_nickname(nb_human_players))

        # The 1st player should be not the 1st to play, if the whole players are human.
        if nb_human_players > 1:
            print("{0}{1}{0}".format(self.EOL, self.DIALOGS['shuffle']))
            self.players.shuffle()

        # Display the rules.
        r = "{0}{1}{0}".format(self.EOL, self.rules.DIALOGS['reminder'])
        r += self.rules.before_to_play(nb_human_players, self.players.players[self.players.p_id[0]]['nickname'])
        print(r)

        # Main game loop.
        nickname_away = self.main_loop(nb_human_players)

        # A player want to go away, display HOF.
        if nickname_away:
            if nb_human_players == 1:
                print("{}{}{}".format(5 * self.EOL, self.ai_like.DIALOGS['sly_bye'], self.EOL))

            else:
                to_diag = 5 * self.EOL
                to_diag += self.DIALOGS['a_player_leave'].format(nickname_away)
                to_diag += self.EOL
                print(to_diag)

        self.display_points()

        return 0

######################

if __name__ == "__main__":
    help(Terminal)
    print("Don't launch me directely, please !")
    print("Run python3 shiri-tory.py or directely shiri-tory.py if eXecution right(s) is/are ON.")
    sys.exit(1)
