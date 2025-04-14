from argparse import ArgumentParser
import random
import sys
import board

""" A one player battleship game where the opponent is a computer
"""

class GameState():
    pass

def boardGame(self, rows, columns):
    pass


def winCondition(self, sunken, ships):
    pass

def play(self):
    """ Play Battleship"""
    pass

def main():
    pass

def parse_args(arglist):
    parser = ArgumentParser()
    parser.add_argument("playerName")
    parser.add_argument("computerOption")
    parser.add_argument("")

    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args)
