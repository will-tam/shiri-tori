# -*- coding: utf-8 -*-

# Standard libraries import.

# Third libraries import.
import wx
import wx.adv as wxa

# Projet modules import.
#from utils import win_loose, win_loose_annouce
#import player

######################

class Score(wx.Panel):
    """
    wx.Panel classes derivated class.

    The scores' panel.

    Public attributes.
    """

    # Private attributes.
    # __playersI = instance of players.

    w = 238     # Easy to change width of Panel and ListCtrl.

    # Public methods.
    def __init__(self, parent, playersI, panel_pos=wx.Point(568, 16)):
        """
        __init__ : initiate class
        @parameters : parent = parent of this widget.
                      playersI = instance of players.
        @return : none.
        """
        self.__playersI = playersI

        wx.Panel.__init__(self,
                          parent=parent,
                          id=-1,
                          pos=panel_pos,
                          size=wx.Size(Score.w, 424),
                          style=wx.SIMPLE_BORDER | wx.RAISED_BORDER)

        titles= ["Players", "Won","Lost"]

        self.__listCtrl = wx.ListCtrl(parent=self,
                                      id=-1,
                                      pos=wx.Point(0, 0),
                                      size=wx.Size(Score.w, 552),
                                      style=wx.LC_REPORT)

        for c, t in enumerate(titles):
            w = 38 if c > 0 else 159    # Width is not same according 1st columns and others.

            self.__listCtrl.InsertColumn(col=c,
                                         format=wx.LIST_FORMAT_CENTER,
                                         heading=t,
                                         width=w)

        self.update()

    def update(self):
        """
        Update the scores in the score widget.
        @parameters : none.
        @return : none.
        """
        self.__listCtrl.DeleteAllItems()

        for p in self.__playersI:
            self.__listCtrl.Append(p.tuple_it())

######################

class Hall_of_fames(wx.Frame):
    """
    wx.Frame classes derivated class.

    Resume the score at the end.

    Public attributes.
    """

    # Private attributes.
    # __playersI = instance of players.
    # __nickname_away = Whose player wants to be away.

    # Public methods.
    def __init__(self, parent, playersId, nickname_away):
        """
        __init__ : initiate class
        @parameters : parent = parent of this widget.
                      playersId = players Id.
                      nickname_away = Whose player wants to be away.
        @return : none.
        """
        self.__playersId = playersId
        self.__nickname_away = nickname_away

        # Main frame.
        wx.Frame.__init__(self,
                          parent=parent,
                          id=-1,
                          title="Hall of fames",
                          pos=wx.Point(548, 155),
                          size=wx.Size(568, 515),
                          style=wx.ALWAYS_SHOW_SB)
        self.Center(wx.BOTH)

        # Create the score part. Calling the as-for class.
        Score(self, self.__playersI, panel_pos=wx.Point(0, 0))

        # Create Hall of fames it-self.
        self.__info_panel = wx.Panel(self,
                                     id=-1,
                                     pos=wx.Point(Score.w + 2, 8),
                                     size=wx.Size(568 - Score.w, 400),
                                     style=0)

        label = "Of course, you have feel i was the strongest !" if self.__nb_players == 1\
                else "{} would to get away !!!".format(self.__nickname_away)

        wx.StaticText(parent=self.__info_panel,
                      id=-1,
                      label=label,
                      style=0).Center(wx.HORIZONTAL)

        winners_sw = wx.adv.SashWindow(parent=self.__info_panel,
                                       id=-1,
                                       pos=wx.Point(0, 40),
                                       size=wx.Size(330 - 8, 140),
                                       style=wx.DOUBLE_BORDER | wxa.SW_3DSASH | wxa.SW_3DBORDER | wx.RAISED_BORDER | wxa.SW_3D | wx.CLIP_CHILDREN)

        loosers_sw = wx.adv.SashWindow(parent=self.__info_panel,
                                       id=-1,
                                       pos=wx.Point(0, 200),
                                       size=wx.Size(330 - 8, 140),
                                       style=wx.SIMPLE_BORDER | wx.CLIP_CHILDREN)

        # Annoucement,with grammatical correction, according find winners and loosers players.
        winners, loosers = win_loose(playersI)
        winners_str, loosers_str = win_loose_annouce(len(winners), len(loosers))

        win_lbl="\n\tAnd the {}\n\n".format(winners_str)
        for winner in winners:
            win_lbl += "\t\t" + winner + "\n"

        wx.StaticText(parent=winners_sw,
                      id=-1,
                      label=win_lbl)

        lost_lbl="\n\tSo, the {}\n\n".format(loosers_str)
        for looser in loosers:
            lost_lbl += "\t\t" + looser + "\n"

        wx.StaticText(parent=loosers_sw,
                      id=-1,
                      label=lost_lbl)

        # The close buttons creation.
        self.__btn_close = wx.Button(parent=self,
                                     id=wx.ID_EXIT,
                                     pos=wx.Point(10, 440),
                                     style=0)
        self.__btn_close.Center(wx.HORIZONTAL)
        self.__btn_close.SetFocus()

        # Bind buttons to its event.
        self.__btn_close.Bind(event=wx.EVT_BUTTON,
                              handler=self.__on_btn_close,
                              id=wx.ID_EXIT)

        # Bind to close window event.
        self.Bind(wx.EVT_CLOSE, self.__on_btn_close)  # Same as user press quit button.

    # Private methods.
    def __on_btn_close(self, event):
        """
        On btn_close click event :
            fill the self.palyers_nn with the nickname of each players,
            and destroy this widget.
        @parameters : event = the event which called this function.
        @return : none
        """
        self.Destroy()
        event.Skip()

######################

def hall_of_fame(wx_app, playersId, nickname_away):
    """
    Display Hall of Fame widget.
    @parameters : wx_app = the wx application instance.
                  playersId = players Id.
                  nickname_away = Whose player wants to be away.
    @return : none.
    """
    hof = Hall_of_fames(None, playersId, nickname_away)
    hof.Show()

    wx_app.MainLoop()

######################

if __name__ == "__main__":
    print("Don't launch me directely, please !")
    print("Run python3 shiri-tory.py or directely shiri-tory.py if eXecution right(s) is/are ON.")
    sys.exit(1)
