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

######################

def graphical_mode():
    """
    Main for interface mode.
    @parameters : none.
    @return : 0 = all was good.
    """

    wx_app = wx.App()

    nb_players = HMI_Nb_players.ask_number_of_players(wx_app)
    if nb_players == 0:
        print("\nMaybe later !\n")
        bye_dlg = wx.MessageDialog(parent=None,
                                   message="Maybe later !",
                                   caption="Well !",
                                   style=wx.OK | wx.ICON_INFORMATION)
        bye_dlg.ShowModal()
        bye_dlg.Destroy()
        return 0

    playersI = HMI_Ask_nickname.ask_nickname(wx_app, nb_players)

    print(playersI)

    nickname_away = HMI_Game.ze_GAME(wx_app, playersI, nb_players)

    return 0

######################

if __name__ == "__main__":
    print("Don't launch me directely, please !")
    print("Run python3 shiri-tory.py or directely shiri-tory.py if eXecution right(s) is/are ON.")
    sys.exit(1)