#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# Entry point.

# Standard library import.
import sys
import argparse

# Third-part library import.

# Project library import.
import engine.engine
import HMI.terminal.terminal

######################

def opt_arg(helpme=False):
    """
    Option and arguments parse.
    @parameters : none.
    @return : parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Run shiri-tori game.",
                                     argument_default="help")

    parser.add_argument('-t','--terminal',
                        action="store_true",
                        default=False,
                        help="Run game in terminal/console mode.")

    parser.add_argument('-x','--gfx',
                        action="store_true",
                        default=False,
                        help="Run game with wxPython. /!\ Not implemented yet /!\ ")

    parser.add_argument('-s','--server',
                        type=int,
                        nargs='?',
                        default=False,
                        help="Run server game. /!\ Not implemented yet /!\ ")

    if helpme:
        parser.print_help()
        return False

    return parser.parse_args()

def main(arg):
    """
    Main function.
    @parameters : some arguments, in case of use.
    @return : 0 = all was good.
              ... = some problem occures.
    """

    print("")
    args = opt_arg()
    print(args)

    if args.terminal:
        pass
    elif args.gfx:
        pass
    elif args.server:
        pass
    else:
        opt_arg(helpme=True)

    return 0

######################

if __name__ == "__main__":
    ret_code = main(sys.argv[1:])      # Keep only the argus after the script name.
    sys.exit(ret_code)
