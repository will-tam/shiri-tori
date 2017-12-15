# -*- coding: utf-8 -*-

# Standard libraries import.
import sys

# Third libraries import.
import wx

# Projet modules import.
import player
import one_game
import almostAI

######################

class Game(wx.Frame):
    """
    wx.Frame class derivated class.

    Ask the nickname of each players, according their number.

    Public attributes.
        nickname_away = the nick name of the player who leaves the game.
    """

    # Private attributes.


    # Public methods.

    def __init__(self, parent, playersI, nb_players):
        """
        __init__ : initiate class
        @parameters : playersI = instance of players.
                      nb_players = number of players.
        @return : none.
        """
        self.nickname_away = ""

        # Main frame.
        wx.Frame.__init__(self,
                          parent=parent,
                          id=-1,
                          title="Shiri Tori - \u5c3b\u53d6\u308a",
                          size=wx.Size(559, 477),
                          style=wx.ALWAYS_SHOW_SB)
        self.Center(wx.BOTH)

        #Create a StaticBox widget aka label.
        self.__lbl_previous_player_answer = "... said"
        self.previous_player_answer = wx.StaticBox(parent=self,
                                                   id=wx.ID_ANY,
                                                   label=self.__lbl_previous_player_answer,
                                                   pos=wx.Point(5, 5),
                                                   size=wx.Size(547, 280),
                                                   style=0)

        self.__lbl_player_your_turn = "..., your turn"
        self.player_your_turn = wx.StaticBox(parent=self,
                                             id=wx.ID_ANY,
                                             label=self.__lbl_player_your_turn,
                                             pos=wx.Point(5, 288),
                                             size=wx.Size(547, 120),
                                             style=0)

        # The validation and leaving buttons creation.
        self.btn_validate = wx.Button(parent=self,
                                      id=wx.ID_OK,
                                      pos=wx.Point(219, 360),
                                      size=wx.Size(85, 32),
                                      style=0)

        self.btn_leave = wx.Button(parent=self,
                                   id=wx.ID_EXIT,
                                   label="I want to leave you !!!",
                                   pos=wx.Point(0, 416),
                                   size=wx.Size(557, 35),
                                   style=0)

        # Bind buttons to their events.
        self.btn_validate.Bind(event=wx.EVT_BUTTON,
                               handler=self.__on_btn_validate,
                               id=wx.ID_OK)

        self.btn_leave.Bind(event=wx.EVT_BUTTON,
                            handler=self.__on_btn_leave,
                            id=wx.ID_EXIT)


    # Private methods.
    def __on_btn_validate(self, event):
        """
        On btn_validate click event :
            TODO : COMPLET WHAT HAPPED ON CLICK !!!
        @parameters : event = the event which called this function.
        @return : none
        """
        print("Validation !!!")

    def __on_btn_leave(self, event):
        """
        On btn_leave click event :
            TODO : COMPLET WHAT HAPPED ON CLICK !!!
        @parameters : event = the event which called this function.
        @return : none
        """
        print("bye")
        self.Destroy()

    def __update_previous_player_answer(self):
        """
        Update the static box of the result of checking.
        @parameters : none.
        @return : none.
        """

        self.__lbl_answer_player = "..."
        self.answer_player_lbl= wx.StaticText(parent=self,
                                              id=-1,
                                              label=self.__lbl_answer_player,
                                              pos=wx.Point(70,27),
                                              size=wx.Size(13, 15),
                                              style=0)

        self.checkit_lbl = wx.StaticText(parent=self,
                                         id=-1,
                                         label='Check it ...',
                                         pos=wx.Point(70, 55),
                                         size=wx.Size(69, 15),
                                         style=0)

        self.__lbl_only_hira_lbl="Only Hiragana ?"
        self.only_hira_lbl = wx.StaticText(parent=self,
                                           id=-1,
                                           label=self.__lbl_only_hira_lbl,
                                           pos=wx.Point(119, 79),
                                           size=wx.Size(102, 15),
                                           style=0)




#        self.presence_of_u30_lbl = wx.StaticText(id=wxID_GAMEPRESENCE_OF_U30_LBL,
#              label=u'Presence of \u30fc', name=u'presence_of_u30_lbl',
#              parent=self, pos=wx.Point(119, 103), size=wx.Size(93, 17),
#              style=0)
#
#        self.staticText3 = wx.StaticText(id=wxID_GAMESTATICTEXT3,
#              label='staticText3', name='staticText3', parent=self,
#              pos=wx.Point(119, 128), size=wx.Size(69, 15), style=0)
#
#        self.staticText4 = wx.StaticText(id=wxID_GAMESTATICTEXT4,
#              label='staticText4', name='staticText4', parent=self,
#              pos=wx.Point(119, 150), size=wx.Size(69, 15), style=0)
#
#        self.staticText5 = wx.StaticText(id=wxID_GAMESTATICTEXT5,
#              label='staticText5', name='staticText5', parent=self,
#              pos=wx.Point(119, 175), size=wx.Size(69, 15), style=0)

#        self.staticText1 = wx.StaticText(id=wxID_GAMESTATICTEXT1,
#              label=u'Ok. / Sorry ..., you loose the turn !',
#              name='staticText1', parent=self, pos=wx.Point(70, 201),
#              size=wx.Size(217, 15), style=0)

#        self.staticText2 = wx.StaticText(id=wxID_GAMESTATICTEXT2,
#              label=u'+1 loose point for you, +1 win point for the others',
#              name='staticText2', parent=self, pos=wx.Point(70, 228),
#              size=wx.Size(320, 15), style=0)

    """

        self.answer_entry = wx.TextCtrl(id=wxID_GAMEANSWER_ENTRY,
              name=u'answer_entry', parent=self, pos=wx.Point(80, 320),
              size=wx.Size(376, 25), style=0, value=u'')


    """

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
