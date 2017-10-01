#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Standard library import.
import sys

# Third-part library import.

# Project library import.
import console_mode as cm

######################

def help():
    """
    Display help in console mode.
    @parameters : none.
    @return : none.
    """
    print("\n")
    print("""In this game, a 1st player write a japanese word.
A second player, write a word beggining with the end of the previous one.
And so on.
If a player write a word with a ん or ン ending, he/she looses.""")
    print("\nOptions")
    print("\t-h : this help.")
    print("\t-c : console mode. Default")
    print("\t-g : graphical mode.")
    print("\t-s : server mode. Add this args with one of the 2 before (Not yet implemented.")
    print("\n")

def main(args):
    """
    Main function.
    @parameters : args = some arguments, in case of use.
    @return : 0 = all was good.
              ... = some problem occures.
    """
    if len(args) == 0 or args[0][0] != '-':
        help()
        return 1

    args = "".join([ap.strip("-") for ap in args])

    if "h" in args:
        help()
        return 1

    if "s" in args:
        print("\nNot yet implemented ! Sorry.\n")
        return 1

    if "c" in args:
        cm.console_mode()
        return 0

    if "g" in args:
        pass
        return 0

    return 0

######################

if __name__ == "__main__":
    rc = main(sys.argv[1:])      # Keep only the argus after the script name.
    sys.exit(rc)
