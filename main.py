from argparse import ArgumentParser
import sys

""" A one player battleship game where the opponent is a computer
"""

def play(self):
    """ Play Battleship"""
    pass 

def main():
    pass

def parse_args(arglist):
    parser = ArgumentParser()
    parser.add_argument("")
    parser.add_argument("")
    parser.add_argument("")

    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args)
