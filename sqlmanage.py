# -*- coding: utf-8 -*-

# Standard library import.
import os.path

# Third-part library import.
import sqlalchemy as sqlAl


class SQLManage():
    """
    Manage specifing SQL for the game.
    """
    # Public attributes.


    # Private attributes.
    __DB_NAME = 'sqlite:///goi.sqlite'


    # Public methods.
    def __init__(self):
        """
        __init__ : initiate class.
        @parameters : none.
        @return : none.
        """
        self.__db = sqlAl.create_engine(SQLManage.__DB_NAME, echo=False)   # echo=True for debug.
        self.__metadata =  sqlAl.MetaData(self.__db)
        # Work only on the columnn 'kana' of the 'dict' table.
        self.__goi = sqlAl.Table('dict',
                                 self.__metadata,
                                 sqlAl.Column('kana', sqlAl.String(20)),
                                 sqlAl.Column('rowid', sqlAl.Integer))

    def ask_if_exist_kana(self, kana_to_check):
        """
        Check if a given data is in database.
        @parameters : kana_to_check = the kana to check.
        @return : True => the data has been found, everelse False.
        """
        stmt = self.__goi.select(self.__goi.c.kana == kana_to_check)
        rst = True if stmt.execute().fetchone() else False
        return rst

    def what_at_rowid(self, choosen_rowid):
        """
        Return the field at the row number.
        @parameters : choosen_rowid = the row id to read.
        @return : the found field.
        """
        stmt = self.__goi.select(self.__goi.c.rowid== choosen_rowid)
        rst = True if stmt.execute().fetchone() else False
        return stmt.execute().fetchone()[0]

    def number_of_row(self):
        """
        Return the number of the row.
        @parameters : none.
        @return : return the number of row.
        """
        stmt = sqlAl.select([sqlAl.func.count("*")], from_obj=[self.__goi])
        return stmt.execute().fetchone()[0]

    # Private methods.

######################

def check_slqlite_file():
    """
    Check if the sqlite file exists. The file is the file of the class.
    @parameter : none.
    @return : True => exists, everelse False.
    """
    try:
        db_to_test = SQLManage()
        db_to_test.ask_if_exist_kana("ことば")
        return True
    except:
        return False
