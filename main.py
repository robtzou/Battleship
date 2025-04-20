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
        cpuBoard    = [["~" for _ in range(board_size)] for _ in range(board_size)]
        playerBoard = [["~" for _ in range(board_size)] for _ in range(board_size)]

        # Combine all ship coordinates
        ships = self.backend.battleship + self.backend.submarine + self.backend.destroyer

        # Mark ship positions on the board with "B"
        for x, y in ships:
            # Since Python count starts at zero.
            playerBoard[x - 1][y - 1] = "B"

        # Display boards
        print("CPU Board:")
        print("  " + " ".join(str(i + 1) for i in range(board_size)))
        for i, row in enumerate(cpuBoard):
            print(str(i + 1) + " " + " ".join(row))
        print("  " + " ".join(str(i + 1) for i in range(board_size)))
        print("Player Board:")
        for i, row in enumerate(playerBoard):
            print(str(i + 1) + " " + " ".join(row))

        return playerBoard, cpuBoard

if __name__ == "__main__":
    play = Backend()
    play.shipPlacement()
    visual = Battleship(play)
    visual.boardVisual()
