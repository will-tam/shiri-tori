#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Standard library import.
import unittest

# Third-part library import.

# Project library import.
import player

######################

class Player_Test(unittest.TestCase):
    """
    Test case of class Player.
    """

    def setUp(self):
        """
        Tests init.
        Run on every begining test in this class.
        @parameters : none.
        @return : none.
        """
        self.p = player.Player("Testplayer")

    #@unittest.skip("Not yet fully implemented!!")
    def test___init__(self):
        """
        Test of __init__().
        @parameters : none.
        @return  : none.
        """
        self.assertEqual(self.p.nickname, "Testplayer")
        self.assertEqual(self.p.win_rounds, 0)
        self.assertEqual(self.p.loose_rounds, 0)

    #@unittest.skip("Not yet fully implemented!!")
    def test_add_one_point_win(self):
        """
        Test of add_one_point_win().
        @parameters : none.
        @return  : none.
        """
        self.p.add_one_point_win()
        self.assertNotEqual(self.p.win_rounds, 0)

    #@unittest.skip("Not yet fully implemented!!")
    def test_add_one_point_lost(self):
        """
        Test of add_one_point_lost().
        @parameters : none.
        @return  : none.
        """
        self.p.add_one_point_lost()
        self.assertNotEqual(self.p.loose_rounds, 0)

    def test_find_me_a_nickname(self):
        """
        Test of find_me_a_nickname().
        @parameters : none.
        @return  : none.
        """
        self.assertEqual(player.find_me_a_nickname(0), "Unknown You")
        self.assertEqual(player.find_me_a_nickname(1), "Unknown Player 1")
        self.assertEqual(player.find_me_a_nickname(2), "Unknown Player 2")
        self.assertEqual(player.find_me_a_nickname(3), "Unknown Player 3")
        self.assertEqual(player.find_me_a_nickname(4), "Unknown Player 4")
        self.assertEqual(player.find_me_a_nickname(5), "Unknown Player 5")
