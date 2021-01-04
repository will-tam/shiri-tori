#!/usr/bin/python3
# -*- coding: utf-8 -*-

######################

def xor(a, b):
    """
    Find a XOR b.
    @parameters : a = first term.
                  b = second term.
    @return : a XOR B it self.
    """
    return (not a) & b | a & (not b)

def win_loose(playersI):
    """
    Winners and loosers players annoucement.
    @parameters : playersI = instance of players.
    @return : a tuple of list (winners, loosers).
    """
    # Search the max of each points.
    max_win_points = max([player.win_rounds for player in playersI])
    max_loose_points = max([player.loose_rounds for player in playersI])

    # Pick up the name of each group according the max points of each group.
    winners = [p.nickname for p in playersI if p.win_rounds == max_win_points]
    loosers = [p.nickname for p in playersI if p.loose_rounds == max_loose_points]

    return (winners, loosers)

def win_loose_annouce(nb_winners, nb_loosers):
    """
    Winners and loosers players annoucement.
    @parameters : nb_winners = number of winners.
                  nb_loosers = number of loosers.
    @return : a tuple (winners annoucement, loosers annoucement).
    """
    w_annouce = "winners are" if nb_winners > 1 else "winner is"
    l_annouce = "loosers are" if nb_loosers > 1 else "looser is"

    return (w_annouce, l_annouce)
