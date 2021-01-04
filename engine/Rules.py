# -*- coding: utf-8 -*-

# NOTE: uncomment to debug
print("{}.{}".format(__package__,__name__))

# Standard libraries import.
import sys


# Third libraries import.


# Projet modules import.


######################

class Rules():
    """
    Check if rules are respected.
    Remind them if asked.

    Public attributes.
        controllers : list of adresses of controllers.
    """

    # Private attributes.


    # Public methods.

    def __init__(self):
        """
        __init__ : initiate class
        @parameters : none.
        @return : none.
        """
        self.controllers = [self.controllers0,
                           ]

    def controllers0(self):
        """
        Controller for rule 1 :
        @parameters : none.
        @return : none.
        """
        pass

    def reminder(self):
        """
        Remind the rules.
        @parameters : none.
        @return : the rules sting.
        """
        rules_are = ""
        return rules_are

    # Private methods.


######################

if __name__ == "__main__":
    help(Rules)
    print("Don't launch me directely, please !")
    print("Run python3 shiri-tory.py or directely shiri-tory.py if eXecution right(s) is/are ON.")
    sys.exit(1)
