# -*- coding: utf-8 -*-

# Standard libraries import.
import sys

# Third libraries import.
import wx

# Projet modules import.

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

    # Private attributes.


    # Public methods.
    def __init__(self, parent):
        """
        __init__ : initiate class
        @parameters : parents = the parent widget.
        @return : none.
        """
        self.nb_players = 0     # No player by default. 0 means "quit game".

        # HMI 1st build with boa-constructor and clean-up "by hand".

        # Main frame.
        wx.Frame.__init__(self,
                          parent=parent,
                          id=-1,
                          title="Number of players",
                          size=wx.Size(434, 213),
                          style=wx.ALWAYS_SHOW_SB)
        self.Center(wx.BOTH)

        #Create a StaticText widget aka label.
        label = """Enter the number of player(s) (no more than 5 included)
        \n1 means 2 players, you and ... me !"""
        self.st_label = wx.StaticText(parent=self,
                                      id=-1,
                                      label=label,
                                      pos=wx.Point(40, 16),
                                      size=wx.Size(368, 45),
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

    # Private methods.
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

    def __on_btn_exit(self, event):
        """
        On btn_exit click event :
            nothing is changed, simply destroy this widget.
        @parameters : event = the event which called this function.
        @return : none
        """
        self.Destroy()

######################

def ask_number_of_players(wx_app):
    """
    Entry point of the HMI.
    @parameters : wx_app = the wx application instance.
    @return : number of player choosen.
    """
    nb_players_hmi = Nb_players(None)
    nb_players_hmi.Show()

    wx_app.MainLoop()

    return nb_players_hmi.nb_players

######################

if __name__ == "__main__":
    print("Don't launch me directely, please !")
    print("Run python3 shiri-tory.py or directely shiri-tory.py if eXecution right(s) is/are ON.")
    sys.exit(1)
