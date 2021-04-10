# -*- coding: utf-8 -*-

# Standard libraries import.
import sys

# Third libraries import.
import wx

# Projet modules import.
#import player

######################

class Ask_nickname(wx.Frame):
    """
    wx.Frame class derivated class.

    Ask the nickname of each players, according their number.

    Public attributes.
        players_nn = list of players' nick name.
    """

    EOL = "\n"
    CAPTIONS = {'Players_nickname' : "Pseudo joueurs",}

    # Private attributes.
    # _nicknames = TextCtrl player name entry list.

    # Public methods.
    def __init__(self, parent, nb_players, game_engine):
        """
        __init__ : initiate class
        @parameters : parents = the parent widget.
                      nb_players = number of players.
                      game_engine = engine of the game instance address.
        @return : none.
        """
        self._nicknames = []

        # HMI 1st build with boa-constructor and clean-up "by hand".

        # Main frame.
        wx.Frame.__init__(self,
                          parent=parent,
                          id=-1,
                          title=self.CAPTIONS['Players_nickname'],
                          size=wx.Size(454, 378),
                          style=wx.ALWAYS_SHOW_SB)
        self.Center(wx.BOTH)

        #Create a StaticText widget aka label.
        if nb_players == 1:     # Setting is not same for 1 or several players.
            label = """{}{}{}""".format(game_engine.ai_like.DIALOGS['just_us'],
                                        self.EOL,
                                        game_engine.players.DIALOGS['ask_nickname'])
            lbl_tl = 40     # Label will be put at this top left position.
            default_nn = [game_engine.players.find_me_a_nickname(0), "The Best IA"]
        else:
            label = game_engine.players.DIALOGS['ask_nickname']
            lbl_tl = 35
            default_nn = []
            for i in range(1, nb_players + 1):
                default_nn.append(game_engine.players.find_me_a_nickname(i))   # By default, fill with this.

        self.st_label = wx.StaticText(parent=self,
                                      id=-1,
                                      label=label,
                                      pos=wx.Point(24, 17),
                                      style=0)

        # A StaticText an TextCtrl for each player.
        for i, nn in enumerate(default_nn):

            txt_ctrl_style = 0  # Enable to change text by default.
            if nb_players == 1 and i == 1:
                txt_ctrl_style = wx.TE_READONLY     # The computer's name won't be change.

            i += 1  # Don't start with 0.
            label = game_engine.players.DIALOGS['ask_nickname_multi'].format(i)

            player_lbl = wx.StaticText(parent=self,
                                       id=i,
                                       label=label,
                                       pos=wx.Point(48, lbl_tl + i * 40),
                                       size=wx.Size(70, 15),
                                       style=0)

            player_nn_entry = wx.TextCtrl(parent=self,
                                          id=i,
                                          value=nn,
                                          pos=wx.Point(128, lbl_tl + i * 40),
                                          size=wx.Size(264, 25),
                                          style=txt_ctrl_style)

            self._nicknames.append(player_nn_entry) # Save instance of TextCtrl for 1 player.

        # The ok buttons creation.
        self.btn_ok = wx.Button(parent=self,
                                id=wx.ID_OK,
                                pos=wx.Point(340, 305),
                                size=wx.Size(85, 32),
                                style=0)

        # Bind buttons to its event.
        self.btn_ok.Bind(event=wx.EVT_BUTTON,
                         handler=self.__on_btn_ok,
                         id=wx.ID_OK)

        # Bind keys to buttons events.
        self.Bind(wx.EVT_CHAR_HOOK, self.__onKey)

        # Bind to close window event.
        # Here, it's forbidden to close with an ALT+F4 or "Close" in tray bar.
        self.Bind(wx.EVT_CLOSE, self.__on_widget_close)

    # Private methods.
    def __onKey(self, event):
        """
        On keypress event, bind on the right function.
        @parameters : event = the event which called this function.
        @return : none
        """
        keys_allowed = {wx.WXK_RETURN : self.__on_btn_ok,
                        }

        e = event.GetKeyCode()
        if e in keys_allowed.keys():
            keys_allowed[e](event)
        else:
            event.Skip()

    def __on_widget_close(self, event):
        """
        No, you can't go out now.
        @parameters : event = the event which called this function.
        @return : none
        """
        pass

    def __on_btn_ok(self, event):
        """
        On btn_ok click event :
            fill the self.palyers_nn with the nickname of each players,
            and destroy this widget.
        @parameters : event = the event which called this function.
        @return : none
        """
        self.palyers_nn = [nn.GetLineText(0) for nn in self._nicknames]
        self.Destroy()
        event.Skip()

######################

def ask_nickname(wx_app, nb_players, game_engine):
    """
    Entry point of the HMI.
    @parameters : wx_app = the wx application instance.
                  nb_players = number of players who asking the nickname.
                  game_engine = engine of the game instance address.
    @return : an player(s) instance(s) list.
    """
    playersI = []

    ask_nickname_hmi = Ask_nickname(None, nb_players, game_engine)
    ask_nickname_hmi.Show()

    wx_app.MainLoop()

    return ask_nickname_hmi.palyers_nn

######################

if __name__ == "__main__":
    print("Don't launch me directely, please !")
    print("Run python3 shiri-tory.py or directely shiri-tory.py if eXecution right(s) is/are ON.")
    sys.exit(1)
