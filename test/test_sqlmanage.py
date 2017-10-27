#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Standard library import.
import unittest

# Third-part library import.

# Project library import.
import sqlmanage

######################

class SQLManage_Test(unittest.TestCase):
    """
    Test case of class sqlmanage.
    """

    def setUp(self):
        """
        Tests init.
        Run on every begining test in this class.
        @parameters : none.
        @return : none.
        """
        self.sqlm = sqlmanage.SQLManage()

    #@unittest.skip("Not yet fully implemented!!")
    def test_check___init__(self):
        """
        Test of check_answer().
        @parameters : none.
        @return  : none.
        """
        self.assertIsInstance(self.sqlm, sqlmanage.SQLManage)

    #@unittest.skip("Not yet fully implemented!!")
    def test_ask_if_exist(self):
        """
        Test of ask_if_exist(data_to_check)
        @parameters : none.
        @return  : none.
        """
        # SELECT dict.kana FROM dict WHERE dict.kana = "ooo"
        self.assertFalse(self.sqlm.ask_if_exist("word"))
        self.assertTrue(self.sqlm.ask_if_exist("ことば"))
