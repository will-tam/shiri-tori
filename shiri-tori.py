#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Entry point.

# Standard library import.
import sys
import argparse

# Third-part library import.

# Project library import.
import __init__
import engine.Engine as gengine
import HMI.terminal.terminal as hmiterm


######################

def opt_args(helpme=False):
    """
    Option and arguments parse.
    @parameters : none.
    @return : parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Run shiri-tori game.")

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

    parser.add_argument('--version',
                        action='version',
                        help="Display version.",
                        version="{} ver. {}".format(parser.prog, __init__.__version__))

    if helpme:
        parser.print_help()
        return 2

    return parser.parse_args()

def main(args):
    """
    Main function.
    @parameters : some arguments, in case of use.
    @return : 0 = all was good.
              ... = some problem occures.
    """

    print("")

    if args and args[0] != '-h' and args[0] != '--help':
        args = opt_args()
    else:
        return opt_args(helpme=True)

#    NOTE: uncomment to debug
#    print(args)

    game_engine = gengine.Engine()
#    NOTE: uncomment to debug
#    print(game_engine)

    if args.terminal:
        print("Go terminal")

        return 0

    if args.gfx:
        print("Go wxPython")

        return 0

    if args.server:
        print("Go serveur en ", end='')
        port = args.server
        print("port", port)

        return 0

    return 0

######################

if __name__ == "__main__":
    ret_code = main(sys.argv[1:])      # Keep only the argus after the script name.
    sys.exit(ret_code)
