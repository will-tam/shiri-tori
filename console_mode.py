#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Standard library import.
import sys

# Third-part library import.

# Project library import.
import player
#import players
import one_turn

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
            pass
    return nb_players

def ask_nickname(nb_players):
    """
    Just ask the nickname of each player.
    If there is only one, a second one is adding, the computer it-self.
    @parameters : nb_players = number of player(s).
    @return : an player(s) instance(s) list.
    """
    nickname = []
    playersI = []

    if nb_players == 1:
        print("\n\nOk, it's just beetween you and me\n")
        nickname.append(input("Please, give me your nickname >>> "))
        nickname.append("The Best IA")
    else:
        for i in range(1, nb_players + 1):
            nickname.append(input("Player {} nickname >>> ".format(i)))

    print(nickname)
    return playersI

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
    ask_nickname(nb_players)
#    main_loop(ask_nickname)
    return 0

######################

if __name__ == "__main__":
    print("Don't launch me directely, please !")
    print("Run python3 shiri-tory.py or directely if eXecution right(s) is/are ON.")
    sys.exit(1)

