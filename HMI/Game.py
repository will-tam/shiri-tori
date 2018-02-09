# -*- coding: utf-8 -*-

# Standard libraries import.
import sys
import time
import random as rnd
import threading as thread

# Third libraries import.
import wx

# Projet modules import.
from utils import *
import rules
import player
import one_game
import almostAI

######################

class Game(wx.Frame, thread.Thread):
    """
    wx.Frame and Thread classes derivated class.

    Ask the nickname of each players, according their number.

    Public attributes.
        nickname_away = the nick name of the player who leaves the game.
    """

    # Private attributes.
    # __game = the one_game instance.
    # __nb_players = number of players.
    # __playersI = instance of players.
    # __now_player = the player who plays now.
    # __computer = the computer player.


    # Public methods.

    def __init__(self, parent, playersI, nb_players):
        """
        __init__ : initiate class
        @parameters : playersI = instance of players.
                      nb_players = number of players.
        @return : none.
        """
        thread.Thread.__init__(self)    # The computer's game will be in its own thread.

        self.__game = one_game.One_Game()     # The one_game instance.

        self.__nb_players = nb_players
        self.__playersI = playersI

        self.nickname_away = ""

        # Prepare game's how to according number of player.
        if self.__nb_players == 1:
            self.__now_player = 0
            self.__computer = almostAI.Almost_AI() # If only 1 human, add the computer player.

        else:
            self.__now_player = rnd.randrange(nb_players)  # 1st player is a random choice.

        # Main frame.
        wx.Frame.__init__(self,
                          parent=parent,
                          id=-1,
                          title="Shiri Tori - \u5c3b\u53d6\u308a",
                          size=wx.Size(559, 477),
                          style=wx.ALWAYS_SHOW_SB)
        self.Center(wx.BOTH)

        # Create the checking part.
        # Create a StaticBox widget aka label.
        self.__update_checking_part(first_time=True)

        # Create the answer part.
        # Create a StaticBox widget aka label.
        lbl_player_your_turn = "So, first round {}".format(self.__playersI[self.__now_player].nickname)
        self.player_your_turn = wx.StaticBox(parent=self,
                                             id=wx.ID_ANY,
                                             label=lbl_player_your_turn,
                                             pos=wx.Point(5, 288),
                                             size=wx.Size(547, 120),
                                             style=0)

        self.player_answer = wx.TextCtrl(parent=self,
                                         id=wx.ID_ANY,
                                         pos=wx.Point(0, 320),
                                         size=wx.Size(376, 25),
                                         style=0)
        self.player_answer.Center(wx.HORIZONTAL)

        # The validation and leaving buttons creation.
        self.btn_validate = wx.Button(parent=self,
                                      id=wx.ID_OK,
                                      pos=wx.Point(219, 360),
                                      size=wx.Size(85, 32),
                                      style=0)
        self.btn_validate.Center(wx.HORIZONTAL)

        self.btn_leave = wx.Button(parent=self,
                                   id=wx.ID_EXIT,
                                   label="I want to leave you !!!",
                                   pos=wx.Point(0, 416),
                                   size=wx.Size(557, 35),
                                   style=0)

        # Some binding events :
        # Bind buttons to their events.
        self.btn_validate.Bind(event=wx.EVT_BUTTON,
                               handler=self.__on_btn_validate,
                               id=wx.ID_OK)

        self.btn_leave.Bind(event=wx.EVT_BUTTON,
                            handler=self.__on_btn_leave,
                            id=wx.ID_EXIT)

    def run(self):
        """
        The thread it-self.
        @parameters : none.
        @return : none
        """
        pass

    def stop(self):
        """
        Stop the thread.
        @parameters : none.
        @return : none
        """
        pass


    # Private methods.
    def __on_btn_validate(self, event):
        """
        On btn_validate click event.
        @parameters : event = the event which called this function.
        @return : none
        """
        print("From {} To validate".format(self.__playersI[self.__now_player].nickname), end=" ")

        self.__game.p_answer = self.player_answer.GetLineText(0)
        print(self.__game.p_answer)

        self.__update_checking_part()

        self.player_your_turn.Label = self.__update_player()

        # --- Si prochain joueur c'est lui, il rentre dans cette fonction de jeu
        if self.__nb_players == 1 and self.__now_player == 1:
            self.__computer_turn()

        if event:
            event.Skip()

    def __on_btn_leave(self, event):
        """
        On btn_leave click event.
            TODO : COMPLET WHAT HAPPED ON CLICK !!!
        @parameters : event = the event which called this function.
        @return : none
        """
        self.stop()     # the thread.

        self.Destroy()  # the window.
        event.Skip()

    def __update_checking_part(self, first_time=False):
        """
        Update the checking part of the answer.
        First time, it shows the HowTo play message.
        @parameters : first_time = show or not the HowTo play message (default = False).
        @result : none.
        """
        if first_time:
            self.previous_player_answer = wx.StaticBox(parent=self,
                                                       id=wx.ID_ANY,
                                                       label="Before to play",
                                                       pos=wx.Point(5, 5),
                                                       size=wx.Size(547, 280),
                                                       style=0)
            self.inside = wx.StaticText(parent=self.previous_player_answer,
                                        label=rules.before_to_play(self.__nb_players, self.__now_player, self.__playersI),
                                        pos=wx.Point(70, 55),
                                        style=0)
            self.inside.Center(wx.BOTH)

        else:
            self.player_answer.Value = ""

            self.previous_player_answer.Label = "{} said {}. Check it ...".format(self.__playersI[self.__now_player].nickname, self.__game.p_answer)

            ca = self.__game.check_answer()
            self.inside.Label = ca[1]

            self.player_answer.SetFocus()

    def __update_player(self):
        """
        Update the player number who it's the turn.
        @parameters : none.
        @result : the nick name of player.
        """
        # Go to the next palyer.
        if self.__nb_players == 1:     # 1 player case.
            self.__now_player = xor(self.__now_player, 1) # Or player[0] or  player[1] ONLY !!!
            if self.__now_player == 1:
                player_turn_nn= "My turn"
            else:
                player_turn_nn = "Your turn {}".format(self.__playersI[self.__now_player].nickname)

        else:
            # Several players case.
            self.__now_player = 0 if self.__now_player == self.__nb_players - 1 else self.__now_player + 1
            player_turn_nn = "{}, your turn".format(self.__playersI[self.__now_player].nickname)

        print(player_turn_nn)
        return player_turn_nn

    def __computer_turn(self):
        """
        Update the player number who it's the turn.
        @parameters : none.
        @result : the nick name of player.
        """
        p_answer = self.__computer.choice(self.__game.p_answer[-1]) if self.__game.p_answer else self.__computer.choice()

        # As humain about type simulation !
        for c in p_answer:
            self.player_answer.AppendText(c)
            # Would type the answer char by char, BUT, doesn't update beetween it.
#            time.sleep(0.5)
#            self.player_answer.Update()

        self.__on_btn_validate(None)


######################

def ze_GAME(wx_app, playersI, nb_players):
    """
    Entry point of the HMI.
    @parameters : wx_app = the wx application instance.
                  playersI = instance of players.
                  nb_players = number of players who asking the nickname.
    @return : who stop the game.
    """
    game_hmi = Game(None, playersI, nb_players)
    game_hmi.Show()

    wx_app.MainLoop()

    return "Him/her"

######################

if __name__ == "__main__":
    print("Don't launch me directely, please !")
    print("Run python3 shiri-tory.py or directely shiri-tory.py if eXecution right(s) is/are ON.")
    sys.exit(1)
