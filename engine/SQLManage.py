# -*- coding: utf-8 -*-

# NOTE: uncomment to debug
print("{}.{}".format(__package__,__name__))

# Standard libraries import.
import sys
import os

# Third libraries import.
import sqlalchemy as sqlAl

# Projet modules import.


######################

class SQLManage():
    """
    Manage specifing SQL for the japanese dictionnary database goi.sqlite

    Public attributes.
    """

    # Private attributes.
    __DB_NAME = os.path.dirname(__file__) + os.sep + 'goi.sqlite'
    __DB_ENGINE = 'sqlite:///' + __DB_NAME

    # Public methods.

    def __init__(self):
        """
        __init__ : initiate class
        @parameters : none.
        @return : none.
        """
#       NOTE: uncomment to debug
        print("SQL init")

        if not os.path.isfile(SQLManage.__DB_NAME):
            raise OSError("{} introuvable".format(SQLManage.__DB_NAME))

        self.__db = sqlAl.create_engine(SQLManage.__DB_ENGINE, echo=False)   # echo=True for debug.
        self.__metadata =  sqlAl.MetaData(self.__db)
        # Work only on the columnn 'kana' of the 'dict' table.
        self.__goi = sqlAl.Table('dict',
                                 self.__metadata,
                                 sqlAl.Column('kana', sqlAl.String(20)),
                                 sqlAl.Column('rowid', sqlAl.Integer))

        if not self.ask_if_exist_kana("ことば"):
            raise ValueError ("Mot de vérification introuvable. La base est-elle bien formée ?")

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

if __name__ == "__main__":
    help(SQL)
    print("Don't launch me directely, please !")
    print("Run python3 shiri-tory.py or directely shiri-tory.py if eXecution right(s) is/are ON.")
    sys.exit(1)
