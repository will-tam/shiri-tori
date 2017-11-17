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
    def test_ask_if_exist_kana(self):
        """
        Test of ask_if_exist_kana(data_to_check)
        @parameters : none.
        @return  : none.
        """
        # SELECT dict.kana FROM dict WHERE dict.kana = "..."
        self.assertFalse(self.sqlm.ask_if_exist_kana("word"))
        self.assertTrue(self.sqlm.ask_if_exist_kana("ことば"))

    #@unittest.skip("Not yet fully implemented!!")
    def test_what_at_rowid(self):
        """
        Test of what_at_rowid(choosen_rowid)
        @parameters : none.
        @return  : none.
        """
        self.assertEqual(self.sqlm.what_at_rowid(1), "あい", "Please check your goi.sqlite")

    #@unittest.skip("Not yet fully implemented!!")
    def test_check_slqlite_file(self):
        """
        Test of check_slqlite_file()
        @parameters : none.
        @return  : none.
        """
        self.assertTrue(sqlmanage.check_slqlite_file())

    #@unittest.skip("Not yet fully implemented!!")
    def test_number_of_row(self):
        """
        Test of number_of_row()
        @parameters : none.
        @return  : none.
        """
        self.assertEqual(self.sqlm.number_of_row(), 139112)
