# -*- coding: utf-8 -*-

# Standard libraries import.

# Third libraries import.
import wx

# Projet modules import.
import player

######################

class Score(wx.Panel):
    """
    wx.Panel classes derivated class.

    The scores' panel.

    Public attributes.
    """

    # Private attributes.
    # __playersI = instance of players.


    # Public methods.
    def __init__(self, parent, playersI):
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
                          pos=wx.Point(568, 16),
                          size=wx.Size(248, 424),
                          style=wx.SIMPLE_BORDER | wx.RAISED_BORDER)

        titles= ["Players", "Won","Lost"]

        self.__listCtrl = wx.ListCtrl(parent=self,
                                      id=-1,
                                      pos=wx.Point(0, 0),
                                      size=wx.Size(248, 552),
                                      style=wx.LC_REPORT)

        for c, t in enumerate(titles):
            self.__listCtrl.InsertColumn(col=c,
                                         format=wx.LIST_FORMAT_LEFT,
                                         heading=t,
                                         width=-1)

        self.update()

    def update(self):
        """
        Update the scores in the score widget.
        @parameters : none.
        @return : none.
        """
        print(self.__playersI)
        self.__listCtrl.DeleteAllItems()

        for p in self.__playersI:
            self.__listCtrl.Append(p.tuple_it())


######################

if __name__ == "__main__":
    print("Don't launch me directely, please !")
    print("Run python3 shiri-tory.py or directely shiri-tory.py if eXecution right(s) is/are ON.")
    sys.exit(1)
