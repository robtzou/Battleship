from board import Backend

""" A one player version of speed-battleship where 
    the opponent is a computer.
    One Battleship - 4
    One Submarine  - 3
    One Destroyer  - 2
"""

class Battleship:

    def __init__(self, backend_instance):
        self.backend = backend_instance

    def boardVisual(self):
        board_size = self.backend.board_size

        # Make a fresh copy of the board
        visual_board = [["~" for _ in range(board_size)] for _ in range(board_size)]

        # Combine all ship coordinates
        ships = self.backend.battleship + self.backend.submarine + self.backend.destroyer

        # Mark ship positions on the board with "B"
        for x, y in ships:
            # Adjust for 1-based to 0-based indexing
            visual_board[x - 1][y - 1] = "B"

        # Display board
        print("  " + " ".join(str(i + 1) for i in range(board_size)))
        for i, row in enumerate(visual_board):
            print(str(i + 1) + " " + " ".join(row))

        return visual_board


if __name__ == "__main__":
    play = Backend()
    visual = Battleship(play)
    visual.boardVisual()
