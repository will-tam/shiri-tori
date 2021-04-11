# -*- coding: utf-8 -*-

# Standard libraries import.
import sys
import time
import random as rnd

# Third libraries import.
import wx

# Projet modules import.
#from utils import *
#import rules
#import player
#import one_game
#import almostAI
#import .Score as HMI_Score
from .Score import Score as HMI_Score

######################

class Game(wx.Frame):
    """
    wx.Frame classes derivated class.

    The main game's window.

    Public attributes.
        nickname_away = the nick name of the player who leaves the game.
        simu_player = the simulate player instance.
    """

    EOL = "\n"
    CAPTIONS = {'before_to_play' : "Avant de jouer",
                'here_we_go' : "C'est parti !",
                'i_wan_to_leave' : "Je veux partir !!!"}

    # Private attributes.
    # __nb_human_players = number of players.
    # __playersId = Players Id adessse.
    # __p_id = the player id who plays now.
    # __player_nn = Player's nickname.
    # __now_player = id of the playing player.
    # __computer = the computer player.
    # __game_engine = engine instance.
    # __first_answer = True if it's a first answer (1st game or after a player has lost). False if next player turn.


    # Public methods.
    def __init__(self, parent, playersId, nb_human_players, game_engine):
        """
        __init__ : initiate class
        @parameters : parent = parent of this widget.
                      playersId = Players Id address.
                      nb_human_players = number of players.
                      game_engine = engine of the game instance address.
        @return : none.
        """
        self.__nb_human_players = nb_human_players
        self.__playersId = playersId
        self.__game_engine = game_engine
        self.__now_player = iter(self.__playersId)

        self.nickname_away = ""

        self.__first_answer = True  # At init, next answer will be the first.

        self.__p_id = next(self.__now_player)

        # Prepare game's how to according number of player.
        if self.__nb_human_players == 1:
#            self.__p_id = self.__game_engine.players.p_id[0]  # 1st player
            self.__computer = self.__game_engine.ai_like # If only 1 human, add the computer "brain".
            self.simu_player = None # The simulate player it-self.

#        else:
#            print(self.__game_engine.players.__p_id, self.__game_engine.players.players)
#            self.__p_id = self.__game_engine.players.p_id[0]  # 1st player is a random choice.

        self.__player_nn = self.__game_engine.players.players[self.__p_id]['nickname']
        print("__init__():", self.__p_id, self.__player_nn)

        # Main frame.
        wx.Frame.__init__(self,
                          parent=parent,
                          id=-1,
                          title="Shiri Tori - \u5c3b\u53d6\u308a",
                          size=wx.Size(865, 477),
                          style=wx.ALWAYS_SHOW_SB)
        self.Center(wx.BOTH)

        # Create the checking part.
        # Create a StaticBox widget aka label.
        self.__update_checking_part(first_time=True)

        # Create the answer part.
        # Create a StaticBox widget aka label.
        lbl_player_your_turn = self.__game_engine.DIALOGS['so_first_round'].format(self.__player_nn)

        self.panel_answer = wx.Panel(parent=self,
                                     id=wx.ID_ANY,
                                     pos=wx.Point(5, 288),
                                     size=wx.Size(547, 120),
                                     style=0)

        self.player_your_turn = wx.StaticBox(parent=self.panel_answer,
                                             id=wx.ID_ANY,
                                             label=lbl_player_your_turn,
                                             pos=wx.Point(0, 0),
                                             size=wx.Size(547, 120),
                                             style=0)

        self.player_answer = wx.TextCtrl(parent=self.panel_answer,
                                         id=wx.ID_ANY,
                                         pos=wx.Point(0, 10),
                                         size=wx.Size(376, 25),
                                         style=0)
        self.player_answer.Center(wx.BOTH)

        # Create the score part. Calling the as-for class.
        self.score = HMI_Score(self, self.__playersId, self.__game_engine)
        self.score.Show()

        # Create the validation and leaving buttons.
        self.btn_validate = wx.Button(parent=self.panel_answer,
                                      id=wx.ID_OK,
                                      pos=wx.Point(0, 80),
                                      size=wx.Size(85, 32),
                                      style=0)
        self.btn_validate.Center(wx.HORIZONTAL)

        self.btn_leave = wx.Button(parent=self,
                                   id=wx.ID_EXIT,
                                   label=self.CAPTIONS['i_wan_to_leave'],
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

        # Bind keys to buttons events.
        self.Bind(wx.EVT_CHAR_HOOK, self.__onKey)

        # Bind to close window event.
        self.Bind(wx.EVT_CLOSE, self.__on_btn_leave)  # Same as user press quit button.

        # Force focus on ...
        self.player_answer.SetFocus()

    def press_btn_validate(self):
        """
        Validation button simulation.
        @parameters : event = the event which called this function.
        @return : none
        """
        self.__on_btn_validate(None)

    # Private methods.
    def __onKey(self, event):
        """
        On keypress event, bind on the right function.
        @parameters : event = the event which called this function.
        @return : none
        """
        keys_allowed = {wx.WXK_ESCAPE : self.__on_btn_leave
                       }

        e = event.GetKeyCode()
        if e in keys_allowed.keys():
            keys_allowed[e](event)
        else:
            event.Skip()

    def __on_btn_validate(self, event):
        """
        On btn_validate click event.
        @parameters : event = the event which called this function.
        @return : none
        """
        self.__game_engine.p_answer = self.player_answer.GetLineText(0)

        self.__update_checking_part()

        # Next player is the computer. Will play after this event.
        if self.__nb_human_players == 1 and self.__p_id == 0:
            wx.CallAfter(self.__computer.HMI_turn, self, self.__game_engine.p_answer)

        self.player_your_turn.Label = self.__update_player()

        self.score.update()

        if event:
            event.Skip()

    def __on_btn_leave(self, event):
        """
        On btn_leave click event.
            TODO : COMPLET WHAT HAPPED ON CLICK !!!
        @parameters : event = the event which called this function.
        @return : none
        """
        self.nickname_away = self.__player_nn
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
            # Modal to explain rules.
            r = "{1}{0}".format(self.EOL, self.__game_engine.rules.DIALOGS['reminder'])
            rules_reminder = wx.MessageDialog(parent=None,
                                              message=r,
                                              caption=self.CAPTIONS['before_to_play'],
                                              style=wx.OK | wx.ICON_INFORMATION)
            rules_reminder.ShowModal()
            rules_reminder.Destroy()

            # Write something start the game.
            r = self.__game_engine.rules.before_to_play(self.__nb_human_players, self.__player_nn)

            self.previous_player_answer = wx.StaticBox(parent=self,
                                                       id=wx.ID_ANY,
                                                       label=self.CAPTIONS['here_we_go'],
                                                       pos=wx.Point(5, 5),
                                                       size=wx.Size(547, 280),
                                                       style=0)
            self.inside = wx.StaticText(parent=self.previous_player_answer,
                                        label=r,
                                        pos=wx.Point(70, 55),
                                        style=0)
            self.inside.Center(wx.BOTH)

        else:
            self.player_answer.Value = ""

            self.previous_player_answer.Label = self.__game_engine.DIALOGS['check_word-gfx'].format(self.__player_nn, self.__game_engine.p_answer)

            checked_answer = self.__game_engine.rules.check_answer(self.__game_engine.p_answer, self.__first_answer)

            if not checked_answer[0]:     # bad answer !
                # Update win and loose points for each players.
                for player_id in self.__game_engine.players.players.keys():
                    if player_id == self.__p_id:
                        self.__game_engine.players.players[player_id]['lost_rounds'] += 1
                    else:
                        self.__game_engine.players.players[player_id]['won_rounds'] += 1

                self.__game_engine.p_answer = ""   # As it was a bad answer, avoid to enter in infinite loop in Almost_AI.choice()
                self.__first_answer = True

            else:
                self.__first_answer = False    # The players are playing.

            self.inside.Label = checked_answer[1]

            self.player_answer.SetFocus()

    def __update_player(self):
        """
        Update the player number who it's the turn.
        @parameters : none.
        @result : the nick name of player.
        """
        # Go to the next palyer.
        print(self.__game_engine.players.p_id)
        print(self.__game_engine.players.players)

        try:
            self.__p_id = next(self.__now_player)
        except StopIteration:
            self.__now_player = iter(self.__playersId)
            self.__p_id = next(self.__now_player)

        self.__player_nn = self.__game_engine.players.players[self.__p_id]['nickname']

        if self.__nb_human_players == 1 and self.__p_id == 1:
                player_turn_nn = self.__game_engine.ai_like.DIALOGS['my_turn']
#            else:
#                player_turn_nn = self.__game_engine.players.DIALOGS['player_name_turn'].format(self.__player_nn)

        else:
            # Several players case.
#            self.p_id = 0 if self.p_id == self.__nb_human_players - 1 else self.p_id + 1
            player_turn_nn = self.__game_engine.players.DIALOGS['player_name_turn'].format(self.__player_nn)

        print("__update_player():", self.__p_id, self.__player_nn)

        return player_turn_nn

######################

def ze_GAME(wx_app, playersId, nb_human_players, game_engine):
    """
    Entry point of the HMI.
    @parameters : wx_app = the wx application instance.
                  playersId = Players Id.
                  nb_human_players = number of players who asking the nickname.
                  game_engine = engine of the game instance address.
    @return : who stop the game.
    """
    game_hmi = Game(None, playersId, nb_human_players, game_engine)

    game_hmi.Show()

    wx_app.MainLoop()

    return game_hmi.nickname_away

######################

if __name__ == "__main__":
    print("Don't launch me directely, please !")
    print("Run python3 shiri-tory.py or directely shiri-tory.py if eXecution right(s) is/are ON.")
    sys.exit(1)
