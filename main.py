from argparse import ArgumentParser
import random
import sys
import board

""" A one player version of speed-battleship where 
    the opponent is a computer.
    One Battleship - 4
    One Submarine  - 3
    One Destroyer  - 2
"""

def shotValid(self):
    if None not in board.coordinates:
        raise ValueError("Shot not within board limits.")

def winCondition(self, sunken, ships):
    pass

def boardVisual(board):
    cpuBoard = ["~" for _ in range(board.board_size) for _ in range(board.board_size)]
    print("  " + " ".join(str(i) for i in range(board.board_size)))
    for column, row in enumerate(board):
        print(str(column) + " " + " ".join(row))
            
    yourBoard = ["~" for _ in range(board.board_size) for _ in range(board.board_size)]
    print("  " + " ".join(str(i) for i in range(board.board_size)))
    for column, row in enumerate(board):
        print(str(column) + " " + " ".join(row))

def play(self):
    """ Play Battleship"""
    pass

def main():
    pass

def parse_args(arglist):
    parser = ArgumentParser()
    parser.add_argument("playerName")
    parser.add_argument("")
    parser.add_argument("")

    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args)
