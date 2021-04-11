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
        size = Width and Heigh size of Score widget dictionnary.
    """

    EOL = "\n"
    CAPTIONS = {'players' : "Joueurs",
                'won' : "Gagnées",
                'lost' : "Perdues"}

    # Private attributes.
    # __playersiId = Players Id address.
    # __game_engine = engine instance.
    # __font_size_listCtrl_w = font size width of listCtrl widget
    # __font_size_listCtrl_h = font size heigh of listCtrl widget

    # Public methods.
    def __init__(self, parent, playersiId, game_engine, panel_pos=wx.Point(568, 16)):
        """
        __init__ : initiate class
        @parameters : parent = parent of this widget.
                      playersiId = Players Id addresse.
                      game_engine = engine of the game instance address.
        @return : none.
        """
        self.__playersiId = playersiId
        self.__game_engine = game_engine

        wx.Panel.__init__(self,
                          parent=parent,
                          id=-1,
                          pos=panel_pos,
                          style=wx.SIMPLE_BORDER | wx.RAISED_BORDER)

        titles = [self.CAPTIONS["players"],
                  self.CAPTIONS["won"],
                  self.CAPTIONS["lost"]]

        self.__listCtrl = wx.ListCtrl(parent=self,
                                      id=-1,
                                      pos=wx.Point(0, 0),
                                      size=(1, 1),
                                      style=wx.LC_REPORT)

        # Need for futur column width ajustment.
        self.__font_size_listCtrl_w, self.__font_size_listCtrl_h = self.__listCtrl.GetFont().GetPixelSize()

        # Prepare headers.
        for c, t in enumerate(titles):
            self.__listCtrl.InsertColumn(col=c,
                                         format=wx.LIST_FORMAT_CENTER,
                                         heading=t)
            self.__listCtrl.SetColumnWidth(c, self.__font_size_listCtrl_w * len(t) + 10)

        self.update()

        # Adjust widgets size.
        w = 0
        for i in range(0, len(titles)):
            w += self.__listCtrl.GetColumnWidth(i)
        h = self.__font_size_listCtrl_h * 8 + 10   # 5 players, header and add a marge.

        self.__listCtrl.SetSize(wx.Size(w, h))
        self.SetSize(wx.Size(w, h))

        # And save it for further use.
        self.size = {}
        self.size['w'], self.size['h'] = self.GetSize()

    def update(self):
        """
        Update the scores in the score widget.
        @parameters : none.
        @return : none.
        """
        self.__listCtrl.DeleteAllItems()

        old_len = 0     # To adjust column width for ListCtrl.
        for player in self.__game_engine.players.players.values():
            player_nn = player['nickname']
            tuple_it = (player_nn, player['won_rounds'], player['lost_rounds'])

            # Adjust column 0 width, if need.
            if old_len < len(player_nn):
                old_len = len(player_nn)
                self.__listCtrl.SetColumnWidth(0, self.__font_size_listCtrl_w * old_len)

            self.__listCtrl.Append(tuple_it)


######################

class Hall_of_fames(wx.Frame):
    """
    wx.Frame classes derivated class.

    Resume the score at the end.

    Public attributes.
    """

    EOL = "\n"
    CAPTIONS = {'hall_of_fames' : "Tableau des scores",
                'here_we_go' : "C'est parti !"}

    # Private attributes.
    # __playersI = instance of players.
    # __nickname_away = Whose player wants to be away.

    # Public methods.
    def __init__(self, parent, playersId, nickname_away, nb_human_players, game_engine):
        """
        __init__ : initiate class
        @parameters : parent = parent of this widget.
                      playersId = players Id.
                      nickname_away = Whose player wants to be away.
                      nb_human_players = number of players.
                      game_engine = engine of the game instance address.
        @return : none.
        """
        self.__playersId = playersId
        self.__nickname_away = nickname_away
        self.__game_engine = game_engine

        # Main frame.
        wx.Frame.__init__(self,
                          parent=parent,
                          id=-1,
                          title=self.CAPTIONS['hall_of_fames'],
#                          pos=wx.Point(548, 155),
                          size=wx.Size(568, 515),
                          style=wx.ALWAYS_SHOW_SB)
        self.Center(wx.BOTH)

        # Create the score part. Calling the as-for class.
        score = Score(self, self.__playersId, game_engine, panel_pos=wx.Point(0, 0))

        # Create Hall of fames it-self.
        self.__info_panel = wx.Panel(self,
                                     id=-1,
                                     pos=wx.Point(score.size['w'] + 2, 8),
                                     size=wx.Size(568 - score.size['w'], 400),
                                     style=wx.SIMPLE_BORDER | wx.RAISED_BORDER)

        label = "{}".format(game_engine.ai_like.DIALOGS['sly_bye']) if nb_human_players == 1\
                else game_engine.DIALOGS['a_player_leave'].format(self.__nickname_away)

        statictext = wx.StaticText(parent=self.__info_panel,
                                   id=-1,
                                   pos=(0, 0),
                                   label=label,
                                   style=0)
        # Cut text length by 2.
        label_half_len = len(label) >> 1
        statictext.Wrap(label_half_len * statictext.GetFont().GetPixelSize()[0])
        statictext.Center(wx.HORIZONTAL)

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
        winners, loosers = game_engine.players.win_loose()
        print(winners, loosers)
#        winners_str, loosers_str = game_engine.win_loose_annouce(len(winners), len(loosers))
#
#        win_lbl="\n\tAnd the {}\n\n".format(winners_str)
#        for winner in winners:
#            win_lbl += "\t\t" + winner + "\n"
#
#        wx.StaticText(parent=winners_sw,
#                      id=-1,
#                      label=win_lbl)
#
#        lost_lbl="\n\tSo, the {}\n\n".format(loosers_str)
#        for looser in loosers:
#            lost_lbl += "\t\t" + looser + "\n"
#
#        wx.StaticText(parent=loosers_sw,
#                      id=-1,
#                      label=lost_lbl)

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

        # Size adjustement.
        statictext_size = statictext.DoGetSize()
        print(statictext_size)

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

def hall_of_fame(wx_app, playersId, nickname_away, nb_human_players, game_engine):
    """
    Display Hall of Fame widget.
    @parameters : wx_app = the wx application instance.
                  playersId = players Id.
                  nickname_away = Whose player wants to be away.
                  nb_human_players = number of players.
                  game_engine = engine of the game instance address.
    @return : none.
    """
    hof = Hall_of_fames(None, playersId, nickname_away, nb_human_players, game_engine)
    hof.Show()

    wx_app.MainLoop()

######################

if __name__ == "__main__":
    print("Don't launch me directely, please !")
    print("Run python3 shiri-tory.py or directely shiri-tory.py if eXecution right(s) is/are ON.")
    sys.exit(1)
