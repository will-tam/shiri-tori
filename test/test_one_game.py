#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Standard library import.
import unittest

# Third-part library import.

# Project library import.
import one_game

######################

class One_Game_Test(unittest.TestCase):
    """
    Test case of class One_Game.
    """

    def setUp(self):
        """
        Tests init.
        Run on every begining test in this class.
        @parameters : none.
        @return : none.
        """
        self.o_g = one_game.One_Game()

    #@unittest.skip("Not yet fully implemented!!")
    def test_check_answer(self):
        """
        Test of check_answer().
        @parameters : none.
        @return  : none.
        """
        self.assertFalse(self.o_g.check_answer("only alphabet"))   # No alphabet letters.
        self.assertTrue(self.o_g.check_answer("ひらがな"))          # Only hiragana.
        self.assertFalse(self.o_g.check_answer("ひらganaだkeだ"))   # Same.
        self.assertFalse(self.o_g.check_answer("パン"))            # Same.
        self.assertTrue(self.o_g.check_answer("じしょ"))           # Same but しょ-like problem
        self.assertFalse(self.o_g.check_answer("ちゃわん"))         # No "ん" at last.
        self.assertFalse(self.o_g.check_answer("んです"))           # No "ん" at first.
        self.assertFalse(self.o_g.check_answer(""))                # Nothing written.
        self.assertFalse(self.o_g.check_answer("るーる"))           # No "ー".
        self.assertFalse(self.o_g.check_answer("ヴィデオ・カセット")) # No "・".
        self.assertTrue(self.o_g.check_answer("まだ"))  # Play a correct word.
        self.assertFalse(self.o_g.check_answer("まだ"))  # Play a correct word but already played.
        self.assertTrue(self.o_g.check_answer("りけんや"))           # In dictionnary (yes it same as "Only hiragana".
