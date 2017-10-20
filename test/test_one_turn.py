#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Standard library import.
import unittest

# Third-part library import.

# Project library import.
import one_turn

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
        self.o_t = one_turn.One_Turn()

    #@unittest.skip("Not yet fully implemented!!")
    def test_check_answer(self):
        """
        Test of check_answer().
        @parameters : none.
        @return  : none.
        """
        self.assertFalse(self.o_t.check_answer("only alphabet"))
        self.assertTrue(self.o_t.check_answer("ひらがなだけだ"))
        self.assertFalse(self.o_t.check_answer("ひらganaだkeだ"))
        self.assertFalse(self.o_t.check_answer("ちゃわん"))
        self.assertFalse(self.o_t.check_answer("パン"))
        self.assertFalse(self.o_t.check_answer(""))
