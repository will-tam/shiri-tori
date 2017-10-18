#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Standard library import.
import unittest

# Third-part library import.

# Project library import.
from console_mode import *
import player

######################

class Console_mode_Test(unittest.TestCase):
    """
    Test case of class One_Turn.
    """

    #@unittest.skip("Not yet fully implemented!!")
    def test_xor(self):
        """
        Test of xor().
        @parameters : none.
        @return  : none.
        """
        self.assertEqual(xor(0, 0), 0)
        self.assertEqual(xor(0, 1), 1)
        self.assertEqual(xor(1, 0), 1)
        self.assertEqual(xor(1, 1), 0)

    #@unittest.skip("Not yet fully implemented!!")
    def test_ask_nickname(self):
        """
        Test of ask_nickname().
        @parameters : none.
        @return  : none.
        """
        self.pi1 = ask_nickname(1)
        self.assertEqual(len(self.pi1), 2)
        self.assertIsInstance(self.pi1[0], player.Player)
        self.assertEqual(self.pi1[1].nickname, "The Best IA")

        self.pi3 = ask_nickname(3)
        self.assertEqual(len(self.pi3), 3)

    #@unittest.skip("Not yet fully implemented!!")
    def test_display_points(self):
        """
        Test of display_points().
        @parameters : none.
        @return  : none.
        """
        print("\n")
        pi = [player.Player("Player {}".format(i)) for i in range(0, 3)]
        pi[2].win_rounds = 100
        pi[0].loose_rounds = 500
        pi[1].win_rounds = 50
        pi[1].loose_rounds = 50
        display_points(pi)
