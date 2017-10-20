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
        self.a_AI = almostAI.Almost_AI()

    #@unittest.skip("Not yet fully implemented!!")
    def test_check_answer(self):
        """
        Test of check_answer().
        @parameters : none.
        @return  : none.
        """
        pass
