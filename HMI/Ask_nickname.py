# -*- coding: utf-8 -*-

# Standard libraries import.
import sys

# Third libraries import.
import wx

# Projet modules import.
import player

######################

class Ask_nickname(wx.Frame):
    """
    wx.Frame class derivated class.

    Ask the nickname of each players, according their number.

    Public attributes.
        players_nn = list of players' nick name.
    """

    # Private attributes.
    # __players_nn_entry = TextCtrl player name entry list.

    # Public methods.
    def __init__(self, parent, nb_players):
        """
        __init__ : initiate class
        @parameters : parents = the parent widget.
                      nb_players = number of players.
        @return : none.
        """
        self.__players_nn_entry = []

        # HMI 1st build with boa-constructor and clean-up "by hand".

        # Main frame.
        wx.Frame.__init__(self,
                          parent=parent,
                          id=-1,
                          title="Players' nickname",
                          size=wx.Size(454, 378),
                          style=wx.ALWAYS_SHOW_SB)
        self.Center(wx.BOTH)

        #Create a StaticText widget aka label.
        if nb_players == 1:     # Setting is not same for 1 or several players.
            label = """Ok, it's just beetween you and me !
            \nPlease, give me your nickname"""
            lbl_tl = 40     # Label will be put at this top left position.
            default_nn = [player.find_me_a_nickname(0), "The Best IA"]
        else:
            label = "Please enter your nickname :"
            lbl_tl = 35
            default_nn = []
            for i in range(1, nb_players + 1):
                default_nn.append(player.find_me_a_nickname(i))   # By default, fill with this.

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
            label = "Player {}".format(i)

            player_lbl = wx.StaticText(parent=self,
                                       id=i,
                                       label=label,
                                       pos=wx.Point(48, lbl_tl + i * 40),
                                       size=wx.Size(56, 15),
                                       style=0)

            player_nn_entry = wx.TextCtrl(parent=self,
                                          id=i,
                                          value=nn,
                                          pos=wx.Point(128, lbl_tl + i * 40),
                                          size=wx.Size(264, 25),
                                          style=txt_ctrl_style)

            self.__players_nn_entry.append(player_nn_entry) # Save instance of TextCtrl for 1 player.

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


    # Private methods.
    def __on_btn_ok(self, event):
        """
        On btn_ok click event :
            fill the self.palyers_nn with the nickname of each players,
            and destroy this widget.
        @parameters : event = the event which called this function.
        @return : none
        """
        self.palyers_nn = [nn.GetLineText(0) for nn in self.__players_nn_entry]
        self.Destroy()
        event.Skip()

######################

def ask_nickname(wx_app, nb_players):
    """
    Entry point of the HMI.
    @parameters : wx_app = the wx application instance.
                  nb_players = number of players who asking the nickname.
    @return : an player(s) instance(s) list.
    """
    playersI = []

    ask_nickname_hmi = Ask_nickname(None, nb_players)
    ask_nickname_hmi.Show()

    wx_app.MainLoop()

    # Intances of players.
    for nickname in ask_nickname_hmi.palyers_nn:
        pi = player.Player(nickname)
        playersI.append(pi)

    return playersI

######################

if __name__ == "__main__":
    print("Don't launch me directely, please !")
    print("Run python3 shiri-tory.py or directely shiri-tory.py if eXecution right(s) is/are ON.")
    sys.exit(1)
