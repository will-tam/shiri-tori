#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Standard library import.
import sys
import wx

# Third-part library import.

# Project library import.
import HMI.Nb_players as HMI_Nb_players
import HMI.Ask_nickname as HMI_Ask_nickname
import HMI.Game as HMI_Game
import HMI.Score as HoF

######################

def graphical_mode():
    """
    Main for interface mode.
    @parameters : none.
    @return : 0 = all was good.
    """
    wx_app = wx.App()

    # Prepare game's how to according number of player.
    nb_players = HMI_Nb_players.ask_number_of_players(wx_app)
    if nb_players == 0:
        say_bye()
        return 0

    # Who are players ?
    playersI = HMI_Ask_nickname.ask_nickname(wx_app, nb_players)

    # Playing !
    nickname_away = HMI_Game.ze_GAME(wx_app, playersI, nb_players)

    HoF.hall_of_fame(wx_app, playersI, nb_players, nickname_away)

#    say_bye()      # TODO : Enlever le #

    return 0

def say_bye():
    """
    Bye bye dialog box.
    @parameters : none.
    @return : none.
    """
    bye_dlg = wx.MessageDialog(parent=None,
                               message="Maybe later !",
                               caption="Well !",
                               style=wx.OK | wx.ICON_INFORMATION)
    bye_dlg.ShowModal()
    bye_dlg.Destroy()

######################

if __name__ == "__main__":
    print("Don't launch me directely, please !")
    print("Run python3 shiri-tory.py or directely shiri-tory.py if eXecution right(s) is/are ON.")
    sys.exit(1)
