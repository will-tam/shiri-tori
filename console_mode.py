#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Standard library import.
import sys
import random as rnd

# Third-part library import.

# Project library import.
import player
#import players
import one_turn
import almostAI

######################

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
    nb_players = 6
    while nb_players > 5:
        try:
            nb_players = int(input(question))
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
        print("\n\nOk, it's just beetween you and me\n")
        nicknames.append(input("Please, give me your nickname >>> "))
        nicknames.append("The Best IA")
    else:
        for i in range(1, nb_players + 1):
            nicknames.append(input("Player {} nickname >>> ".format(i)))

    for nickname in nicknames:
        pi = player.Player(nickname)
        playersI.append(pi)

#    print(nickname)
    return playersI

def main_loop(playersI, nb_players):
    """
    The game main loop.
    @parameters : playersI = intance of the players.
                  nb_players = number of players.
    @return : name of the player who gets away.
    """
    print("playersI =>", playersI)

    game = one_turn.One_Turn()

    if nb_players == 1:
        some_rules = "I'm great lord, I let you begin {}.\n".format(playersI[0].nickname)
        some_rules += "If you are to scarry, enter 0 now or "
        some_rules += "anytime you want!" + 2 * "\n"
        now_player = 0
        computer = almostAI.Almost_AI()
    else:
        some_rules = "Well, let the random deciding who will begin.\n"
        some_rules += "If one among you is to afraid, enter 0 "
        some_rules += "at your turn.\n"
        now_player = rnd.randrange(nb_players)
        some_rules += "So, the first of you will be {}".format(playersI[now_player].nickname)
        some_rules += 2 * "\n"

    print(80*"\n")
    print(some_rules)

    p_answer = ""

    while p_answer != "0":
        if nb_players == 1 and now_player == 1:
            p_answer = computer.choice()
            print("My turn >>> {}".format(p_answer))
#            now_player = 0
        else:
            print("{} your turn >>>".format(playersI[now_player].nickname), end='')
            p_answer = input(" ")
            if p_answer == "0":
                return playersI[now_player].nickname
#            now_player += 1

#        print("{} your turn >>>".format(playersI[now_player].nickname), end="")
#        p_answer = input(" ")
#        if p_answer == 0:
#            break
#        if nb_players == 1:
#            now_player += 1
##            if now_player == 1:
#            print("My turn >>> {}".format(computer.choice()))
##                print("My turn >>> {}".format(computer.choice()))
#            now_player = 0
#        else:
#            pass

        if not game.check_answer(p_answer):
            if nb_players == 1 and now_player == 1:
                print("Oooh sh... you win {} !\n".format(playersI[0].nickname))
                print("+1 win point for you, +1 loose point for ... me !\n\n")

            elif nb_players == 1 and now_player == 0:
                print("I win, you loose {}\n".format(playersI[0].nickname))
                print("+1 win point for me, +1 loose point for YOU !\n\n")

            else:
                print("Sorry {}, you loose the turn !\n".format(playersI[now_player].nickname))
                print("+1 loose point for you, +1 win point for the others\n\n")

            for pI, lostV in enumerate(playersI):
                if pI == now_player:
                    playersI[pI].loose_rounds += 1
                else:
                    playersI[pI].win_rounds += 1

            print(playersI)

        if nb_players == 1:
            now_player = XOR now_player # <<<< C'EST QUOI DEJA LE XOR EN PYTHON ????
        now_player = 0 if now_player == nb_players - 1 else now_player + 1
        print(nb_players, now_player)


def console_mode():
    """
    Main function.
    @parameters : some arguments, in case of use.
    @return : 0 = normal exit.
              ... = some problem occures.
    """
    nb_players = ask_number_of_players()
    if nb_players == 0:
        print("\nMaybe later !\n")
        return 0
    nickname_away = main_loop(ask_nickname(nb_players), nb_players)
    if nickname_away:
        if nb_players == 1:
            print("{}Of course, you have feel i was the strongest !\n".format(5 * "\n"))
        else:
            print("{}{} wants to get away !!!\n".format(5 * "\n", nickname_away))

    return 0

######################

if __name__ == "__main__":
    print("Don't launch me directely, please !")
    print("Run python3 shiri-tory.py or directely if eXecution right(s) is/are ON.")
    sys.exit(1)
