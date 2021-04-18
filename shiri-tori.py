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
import HMI.terminal.Terminal as hmiterm
import HMI.gfx.Gfx as hmigfx


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

#    print(args.__dict__)

#    game_engine = gengine.Engine()
#    NOTE: uncomment to debug
#    print(game_engine)

    if args.terminal:
#       NOTE: uncomment to debug
#        print("Go terminal")
        return hmiterm.Terminal().main()

    if args.gfx:
#       NOTE: uncomment to debug
#        print("Go wxPython")
        return hmigfx.Gfx().main()

    if args.server:
#       NOTE: uncomment to debug
        print("Go serveur en ", end='')
        port = args.server
        print("port", port)

        return 0

    print("option looked like good, but something went wrong !")
    return 1

######################

if __name__ == "__main__":
    ret_code = main(sys.argv[1:])      # Keep only the argus after the script name.
    sys.exit(ret_code)
