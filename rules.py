#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Contains only the game's rules.
"""

rules = """In this game, a 1st player write a japanese word.
A second player, write a word beggining with the end of the previous one.
And so on.
If a player write a word with a ん or ン ending, he/she looses.
The forbidden words are :
    - only one mora words is forbidden (eg: い(胃) - stomach / か　蚊 - mosquito) ;
    - acronym (eg : ヴィップ - VIP) ;
    - a ん beggining word (eg : んです) ;
    - written in katakana words (eg : アルバイト - part time job /　イノシシ - wild boar);
    - contain "ー" (eg : ルール - rule) or "・" (eg : ちきん・なげっと or チキン・ナゲット - chicken nugget) words.

"""

def how_to(nb_players, now_player, playersI):
    """
    Return the how to depending the number of players
    @parameters : nb_players = number of players.
                  now_player = the player who will begin.
                  playersI = players' instance.
    @return : the how to.
    """
    if nb_players == 1:
        howto = "I'm great lord, I let you begin {}.\n".format(playersI[0].nickname)
        howto += "If you are to scarry, enter 0 now or "
        howto += "anytime you want!" + 2 * "\n"
    else:
        howto = "Well, let the random deciding who will begin.\n"
        howto += "If one among you is to afraid, enter 0 "
        howto += "at your turn.\n"
        howto += "So, the first of you will be {}".format(playersI[now_player].nickname)
        howto += 2 * "\n"

    return howto
