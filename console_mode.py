#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Standard library import.
import sys
import random as rnd

# Third-part library import.

# Project library import.
import player
import one_game
import almostAI

######################

def xor(a, b):
    """
    Find a XOR b.
    @parameters : a = first term.
                  b = second term.
    @return : a XOR B it self.
    """
    return (not a) & b | a & (not b)

def ask_number_of_players():
    """
    Just Ask the number of player(s).
    Check no more than 5 included.
    0 means end of game.
    @parameters : none.
    @return : the answer.
    """
    print(25 * "\n")
    question = "\nNumber of player(s) beetween 0 and 5 included : \n"
    question += "0 means you want to go away from me.\n"
    question += "1 means 2 players, you and ... me.\n"
    question += "No more than 5 players.\n"
    question += "So >>> "

    nb_players = 6  # We directely enter inside next loop.

    while nb_players > 5:
        try:
            nb_players = int(input(question))   # Only int expected.
        except:
            print("\n\tSorry, i'm waiting just a number.\n")

    return nb_players

def ask_nickname(nb_players):
    """
    Just ask the nickname of each player.
    If there is only one, a second one is adding, the computer it-self.
    @parameters : nb_players = number of player(s).
    @return : an player(s) instance(s) list.
    """
    nicknames = []
    playersI = []

    if nb_players == 1:
        print("\n\nOk, it's just beetween you and me !\n")
        nicknames.append(input("Please, give me your nickname >>> "))
        # Manage the unknown player in single player mode.
        if nicknames[0] == "":
            nicknames[0] = player.find_me_a_nickname(0)
        nicknames.append("The Best IA")     # For 1 player mode, also computer plays.
    else:
        for i in range(1, nb_players + 1):
            nn = input("Player {} nickname >>> ".format(i))
            # Manage the unknown player in several players mode.
            if nn == "":
                nn = player.find_me_a_nickname(i)
            nicknames.append(nn)

    # Intances of players.
    for nickname in nicknames:
        pi = player.Player(nickname)
        playersI.append(pi)

    return playersI

def main_loop(playersI, nb_players):
    """
    The game main loop.
    @parameters : playersI = intance of the players.
                  nb_players = number of players.
    @return : name of the player who gets away.
    """
    game = one_game.One_Game()

    # Prepare game's rule according number of player.
    if nb_players == 1:
        some_rules = "I'm great lord, I let you begin {}.\n".format(playersI[0].nickname)
        some_rules += "If you are to scarry, enter 0 now or "
        some_rules += "anytime you want!" + 2 * "\n"
        now_player = 0
        computer = almostAI.Almost_AI() # If only 1 human, add the computer player.
    else:
        some_rules = "Well, let the random deciding who will begin.\n"
        some_rules += "If one among you is to afraid, enter 0 "
        some_rules += "at your turn.\n"
        now_player = rnd.randrange(nb_players)  # 1st player is a random choice.
        some_rules += "So, the first of you will be {}".format(playersI[now_player].nickname)
        some_rules += 2 * "\n"

    print(80*"\n")
    print(some_rules)

    p_answer = ""   # No player's answer to enter in loop.

    # THE main loop it-self.
    while p_answer != "0":
        if nb_players == 1 and now_player == 1:     # Only 1 player, and it's computer's turn.
            p_answer = computer.choice(p_answer[-1])
            print("My turn >>> {}".format(p_answer))
        else:   # everelse it's player turn (it runs for 1 or several human players).
            print("{}, your turn >>>".format(playersI[now_player].nickname), end='')
            p_answer = input(" ")
            if p_answer == "0":         # 0 means exit game.
                return playersI[now_player].nickname

        if not game.check_answer(p_answer):     # bad answer !
            if nb_players == 1 and now_player == 1:         # Only 1 player and it's the computer's turn.
                print("\tOooh sh... you win {} !\n".format(playersI[0].nickname))
                print("\t+1 win point for you, +1 loose point for ... me !\n")

            elif nb_players == 1 and now_player == 0:       # Only 1 player and it's the human's turn.
                print("\tI win, you loose {}\n".format(playersI[0].nickname))
                print("\t+1 win point for me, +1 loose point for YOU !\n")

            else:       # Several human players.
                print("\tSorry {}, you loose the turn !\n".format(playersI[now_player].nickname))
                print("\t+1 loose point for you, +1 win point for the others\n")

            for pI, lostV in enumerate(playersI):   # Update win and loose points for each players.
                if pI == now_player:
                    playersI[pI].loose_rounds += 1
                else:
                    playersI[pI].win_rounds += 1
            game.playing = False    # The next turn will be a new game.
        else:
            game.playing = True     # The players are playing.
            print("\n")

        # Go to the next palyer.
        if nb_players == 1:     # 1 player case.
            now_player = xor(now_player, 1) # Or player[0] or  player[1] ONLY !!!
        else:
            now_player = 0 if now_player == nb_players - 1 else now_player + 1  # Several players case.

def display_points(playersI):
    """
    Display the win and loose points as a table
    @parameters : playersI = instances' array of players.
    @return : none.
    """
    won_string = "won rounds"
    lost_string = "lost rounds"
    won_string_len = len(won_string)
    lost_string_len = len(lost_string)

    # Take the length of the longest nicknames.
    max_str_len = max([len(player.nickname) for player in playersI])

    # Add the lenth of the 2 strings won_string and lost_string.
    width = max_str_len + won_string_len + lost_string_len

    # Add the border, beetween the 2 strings, beetween nickname and the table body.
    width += 10

    print(width * "*")
    print("* {} * {} * {} *".format(max_str_len * " ", won_string, lost_string))
    for player in playersI:
        pfs = max_str_len - len(player.nickname)    # Number of white spaces after the nickname.
        wfs = won_string_len - len(str(player.win_rounds))      # After the won points.
        plr = lost_string_len - len(str(player.loose_rounds))   # After the lost points.
        print("* {pn}{pfs} * {pwr}{wfs} * {plr}{lfs} *".format(pn = player.nickname,
                                                              pfs = pfs * " ",
                                                              pwr = player.win_rounds,
                                                              wfs = wfs * " ",
                                                              plr = player.loose_rounds,
                                                              lfs = plr * " "))

    print(width * "*", "\n")

    # Search the max of each points.
    max_win_points = max([player.win_rounds for player in playersI])
    max_loose_points = max([player.loose_rounds for player in playersI])

    # Pick up the name of each group according the max points of each group.
    winners = [p.nickname for p in playersI if p.win_rounds == max_win_points]
    loosers = [p.nickname for p in playersI if p.loose_rounds == max_loose_points]

    # Annoucement, with grammatical correction !!!!
    if len(winners) > 1:
        annoucement = "winners are"
    else:
        annoucement = "winner is"

    print("And the {} :".format(annoucement))
    for winner in winners:
        print("\t{}".format(winner))

    if len(loosers) > 1:
        annoucement = "loosers are"
    else:
        annoucement = "looser is"

    print("So, the {} :".format(annoucement))
    for looser in loosers:
        print("\t{}".format(looser))

    print("\n")

def console_mode():
    """
    Main for console mode
    @parameters : none
    @return : 0 = normal exit.
    """
    nb_players = ask_number_of_players()

    if nb_players == 0:
        print("\nMaybe later !\n")
        return 0

    playersI = ask_nickname(nb_players)

    nickname_away = main_loop(playersI, nb_players)

    if nickname_away:
        if nb_players == 1:
            print("{}Of course, you have feel i was the strongest !\n".format(5 * "\n"))

        else:
            print("{}{} would to get away !!!\n".format(5 * "\n", nickname_away))

    display_points(playersI)

    return 0

######################

if __name__ == "__main__":
    print("Don't launch me directely, please !")
    print("Run python3 shiri-tory.py or directely shiri-tory.py if eXecution right(s) is/are ON.")
    sys.exit(1)
