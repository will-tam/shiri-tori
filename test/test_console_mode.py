#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Standard library import.
import unittest

# Third-part library import.

# Project library import.
from console_mode import *
from player import *

######################

class One_Turn_Test(unittest.TestCase):
    """
    Test case of class One_Turn.
    """

    def setUp(self):
        """
        Tests init.
        Run on every begining test in this class.
        @parameters : none.
        @return : none.
        """
        pass

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
        Test of xor().
        @parameters : none.
        @return  : none.
        """
        pi = ask_nickname(1)
        self.assertEqual(len(pi), 2)
        self.assertIsInstance(pi[0], Player)
        self.assertEqual(pi[1].nickname, "The Best IA")

        pi = ask_nickname(3)
        self.assertEqual(len(pi), 3)
