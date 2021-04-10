#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Standard library import.
import sys

# Third-part library import.
import wx

# Project library import.
from ..engine import Engine
import HMI.gfx.Nb_players as HMI_Nb_players
import HMI.gfx.Ask_nickname as HMI_Ask_nickname
import HMI.gfx.Game as HMI_Game
import HMI.gfx.Score as HoF

######################

class Gfx(Engine.Engine):
    """
    Class to manage graphical part of shiri-tori.

    Public attributes.
    """

    EOL = "\n"
    TAB = "\t"
    WAIT_ASK = " >>> "

    CAPTIONS = {'bye' : "Et bien ...",}

    def __init__(self):
        """
        __init__ : initiate class
        @parameters : none.
        @return : none.
        """
        super().__init__()

        self.wx_app = wx.App()

    def say_bye(self):
        """
        Bye bye dialog box.
        @parameters : none.
        @return : none.
        """
        bye_dlg = wx.MessageDialog(parent=None,
                                   message=self.DIALOGS['no_want_play_bye'],
                                   caption=self.CAPTIONS['bye'],
                                   style=wx.OK | wx.ICON_INFORMATION)
        bye_dlg.ShowModal()
        bye_dlg.Destroy()

    def main(self):
        """
        Main function of the gfx IHM.
        @parameters : none.
        @return : 0 = all was good.
        """

        # Prepare game's how to according number of player.
        nb_players = HMI_Nb_players.ask_number_of_players(self.wx_app, self)

        if nb_players == 0:
            self.say_bye()
            return 0

        # Who are players ?
        self.players.register_players(HMI_Ask_nickname.ask_nickname(self.wx_app, nb_players, self))
        self.players.shuffle()

        print(self.players.p_id)
        print(self.players.players)

        # Playing !
#        nickname_away = HMI_Game.ze_GAME(self.wx_app, playersI, nb_players)

#        HoF.hall_of_fame(self.wx_app, playersI, nb_players, nickname_away)

        self.say_bye()

        return 0

######################

if __name__ == "__main__":
    print("Don't launch me directely, please !")
    print("Run python3 shiri-tory.py or directely shiri-tory.py if eXecution right(s) is/are ON.")
    sys.exit(1)
