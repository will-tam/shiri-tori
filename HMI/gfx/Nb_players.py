# -*- coding: utf-8 -*-

# Standard libraries import.
import sys

# Third libraries import.
import wx

# Projet modules import.
from ..engine import Engine

######################

class Nb_players(wx.Frame):
    """
    wx.Frame class derivated class.

    Just ask the number of player(s).
    Check no more than 5 included.
    0 means end of game.

    Public attributes.
        nb_players = save the number of players.
        exit = True if the player wants to leave, everelse False.
    """

    EOL = "\n"
    CAPTIONS = {'number_of_players' : "Nombre de joueurs",}

    # Private attributes.


    # Public methods.
    def __init__(self, parent, game_engine):
        """
        __init__ : initiate class
        @parameters : parents = the parent widget.
                      game_engine = engine of the game instance address.
        @return : none.
        """
        self.nb_players = 0     # No player by default. 0 means "quit game".

        # HMI 1st build with boa-constructor and clean-up "by hand".

        # Main frame.
        wx.Frame.__init__(self,
                          parent=parent,
                          id=-1,
                          title=self.CAPTIONS['number_of_players'],
                          size=wx.Size(434, 213),
                          style=wx.ALWAYS_SHOW_SB)
        self.Center(wx.BOTH)

        #Create a StaticText widget aka label.
        label = """{0}{1}{1}{2}""".format(game_engine.players.DIALOGS['nb_players_question_part_0'],
                                          self.EOL,
                                          game_engine.players.DIALOGS['nb_players_question_part_2'])
        self.st_label = wx.StaticText(parent=self,
                                      id=-1,
                                      label=label,
                                      pos=wx.Point(40, 16),
                                      size=wx.Size(368, 80),
                                      style=0)

        # Create a SpinCtrl widget to enter the number of players.
        self.sc_nb_players = wx.SpinCtrl(parent=self,
                                         id=-1,
                                         pos=wx.Point(213, 94),
                                         size=wx.Size(31, 24),
                                         style=wx.SP_ARROW_KEYS,
                                         min=1,
                                         max=5,
                                         initial=1
                                         )

        # The ok and quit buttons creation.
        self.btn_ok = wx.Button(parent=self,
                                id=wx.ID_OK,
                                pos=wx.Point(46, 136),
                                size=wx.Size(85, 32),
                                style=0)

        self.btn_quit = wx.Button(parent=self,
                                  id=wx.ID_EXIT,
                                  pos=wx.Point(317, 137),
                                  size=wx.Size(85, 32),
                                  style=0)

        # Bind buttons to their events.
        self.btn_ok.Bind(event=wx.EVT_BUTTON,
                         handler=self.__on_btn_ok,
                         id=wx.ID_OK)

        self.btn_quit.Bind(event=wx.EVT_BUTTON,
                           handler=self.__on_btn_exit,
                           id=wx.ID_EXIT)

        # Bind keys to buttons events.
        self.Bind(wx.EVT_CHAR_HOOK, self.__onKey)

        # Bind to close window event.
        # By the the way, it should appear it doesn't need to bind this. But, it's sure of react.
        self.Bind(wx.EVT_CLOSE, self.__on_btn_exit)  # Same as user press quit button.


    # Private methods.
    def __onKey(self, event):
        """
        On keypress event, bind on the right function.
        @parameters : event = the event which called this function.
        @return : none
        """
        keys_allowed = {wx.WXK_RETURN : self.__on_btn_ok,
                        wx.WXK_ESCAPE : self.__on_btn_exit,
                        81 : self.__on_btn_exit
                        }

        e = event.GetKeyCode()
        if e in keys_allowed.keys():
            keys_allowed[e](event)
        else:
            event.Skip()

    def __on_btn_ok(self, event):
        """
        On btn_ok click event :
            fill the self.nb_players with the numberof players,
            and destroy this widget.
        @parameters : event = the event which called this function.
        @return : none
        """
        self.nb_players = self.sc_nb_players.GetValue();
        self.Destroy()
        event.Skip()

    def __on_btn_exit(self, event):
        """
        On btn_exit click event :
            nothing is changed, simply destroy this widget.
        @parameters : event = the event which called this function.
        @return : none
        """
        self.Destroy()
        event.Skip()

######################

def ask_number_of_players(wx_app, game_engine):
    """
    Entry point of the HMI.
    @parameters : wx_app = the wx application instance.
                  game_engine = engine of the game instance address.
    @return : number of player choosen.
    """
    nb_players_hmi = Nb_players(None, game_engine)
    nb_players_hmi.Show()

    wx_app.MainLoop()

    return nb_players_hmi.nb_players

######################

if __name__ == "__main__":
    print("Don't launch me directely, please !")
    print("Run python3 shiri-tory.py or directely shiri-tory.py if eXecution right(s) is/are ON.")
    sys.exit(1)
