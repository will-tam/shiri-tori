#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Standard library import.
import unittest

# Third-part library import.

# Project library import.
import almostAI

######################

class AlmostAI_Test(unittest.TestCase):
    """
    Test case of class almostAI.
    """

    def setUp(self):
        """
        Tests init.
        Run on every begining test in this class.
        @parameters : none.
        @return : none.
        """
        self.a_AI = almostAI.One_Turn()

    #@unittest.skip("Not yet fully implemented!!")
    def test_check_answer(self):
        """
        Test of check_answer().
        @parameters : none.
        @return  : none.
        """
        print("\n")
        self.assertFalse(self.o_t.check_answer("only alphabet"))
        self.assertTrue(self.o_t.check_answer("ひらがなだけだ"))
        self.assertFalse(self.o_t.check_answer("ひらganaだkeだ"))
        self.assertFalse(self.o_t.check_answer("ちゃわん"))
        self.assertFalse(self.o_t.check_answer("パン"))
