# -*- coding: utf-8 -*-

# Standard library import.
import os.path

# Third-part library import.
import sqlalchemy as sqlAl


class SQLManage():
    """
    Manage specifing SQL for the game.

    # Public attributes.
        goi = instance of the sql Table.
    """


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
        self.goi = sqlAl.Table('dict', self.__metadata,
                               sqlAl.Column('kana', sqlAl.String(20))
                              )

    def ask_if_exist(self, data_to_check):
        """
        Check if a given data is in database.
        @parameters : data_to_check = the data to check.
        @return : True => the data has been found, everelse False.
        """
        stmt = self.goi.select(self.goi.c.kana == data_to_check)
        rst = True if stmt.execute().fetchone() else False
        return rst


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
        db_to_test.ask_if_exist("ことば")
        return True
    except:
        return False
