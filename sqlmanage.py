# -*- coding: utf-8 -*-

# Third-part library import.
import sqlalchemy as sqlAl


class SQLManage():
    """
    Manage specifing SQL for the game.

    # Public attributes.
        goi = instance of the sql Table.
    """

    # Private attributes.


    # Private methods.
    __BASENAME = 'sqlite:///dict.sqlite'

    # Public methods.

    def __init__(self):
        """
        __init__ : initiate class.
        @parameters : none.
        @return : none.
        """
        self.__db = sqlAl.create_engine(SQLManage.__BASENAME, echo=False)   # echo=True for debug.
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
