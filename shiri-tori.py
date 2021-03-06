#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Standard library import.
import sys

# Third-part library import.

# Project library import.
import rules
import console_mode as cm
import sqlmanage

import graphical_mode as gm

######################

def help():
    """
    Display help in console mode.
    @parameters : none.
    @return : none.
    """
    print("\n")
    print(rules.rules)
    print("\nOptions")
    print("\t-h : this help.")
    print("\t-c : console mode. Default")
    print("\t-g : graphical mode.")
    print("\t-s : server mode. Add this args with one of the 2 before (Not yet implemented).")
    print("\n")

def main(args):
    """
    Main function.
    @parameters : args = some arguments, in case of use.
    @return : 0 = all was good.
              ... = some problem occures.
    """
    if not sqlmanage.check_slqlite_file():
        print("goi.sqlite database file doesn't exist or corrupted ! I have to stop here !")
        return 1

    if len(args) == 0 or args[0][0] != '-':
        help()
        return 1

    args = "".join([ap.strip("-") for ap in args])

    if "h" in args:     # Help.
        help()
        return 1

    if "s" in args:     # Server mode.
        print("\nNot yet implemented ! Sorry.\n")
        return 1

    if "c" in args:     # Console mode.
        cm.console_mode()
        return 0

    if "g" in args:     # Graphical mode.
        gm.graphical_mode()
        return 0

    return 0

######################

if __name__ == "__main__":
    rc = main(sys.argv[1:])      # Keep only the argus after the script name.
    sys.exit(rc)
