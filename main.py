import random
from board import Backend
from argparse import ArgumentParser
import sys

""" 
    A one player version of speed-battleship where 
    the opponent is a computer.
    One Battleship - 4
    One Submarine  - 3
    One Destroyer  - 2
"""

class Battleship:
    """Displays the game
    Attributes:
        backend_instance: instance of the backend game logic that stores 
            game state, including player shots, hits, and other relevant data.
    """
    def __init__(self, backend_instance):
        """Initializes the board for the game

        Args:
            backend_instance: instance of the backend game logic that stores 
                game state, including player shots, hits, and other relevant data.
        """
        self.backend_instance = backend_instance

    def boardVisual(self):
        """Displays the current visual state of the player's game board.
        The board includes:
            - Player ship positions (marked with "B")
            - CPU hits on player ships (marked with "X")
            - CPU misses (marked with "O")
            - Empty/unknown tiles (marked with "~")
        """
        board_size = 6
        # New board
        visual_board = [["~" for _ in range(board_size)] for _ in range(board_size)]

        player_ships = (
        self.backend_instance.battleship +
        self.backend_instance.submarine +
        self.backend_instance.destroyer
        )

        for x, y in player_ships:
            visual_board[x - 1][y - 1] = "B"
            
        for x, y in self.backend_instance.cpu_hits:
            visual_board[x - 1][y - 1] = "X"
            
        for x, y in self.backend_instance.cpu_shots:
            if (x, y) not in self.backend_instance.cpu_hits:
                visual_board[x - 1][y - 1] = "O"

        print("\nYour Board:")
        print("  " + " ".join(str(i + 1) for i in range(board_size)))
        for i, row in enumerate(visual_board):
            print(str(i + 1) + " " + " ".join(row))

    def cpuVisual(self):
        """Displays the current visual state of the cpu's game board.
        
        This method shows the player's actions on the CPU's board, including:
            - Hits marked with "X"
            - Misses marked with "O"
            - Unknown positions (marked with "~")
        """
        board_size = 6

        visual_board = [["~" for _ in range(board_size)] for _ in range(board_size)]
        
        for x, y in self.backend_instance.player_hits:
            visual_board[x - 1][y - 1] = "X"
            
        for x, y in self.backend_instance.player_shots:
            if (x, y) not in self.backend_instance.player_hits:
                visual_board[x - 1][y - 1] = "O"
        
        print("\nCPU Board:")
        print("  " + " ".join(str(i + 1) for i in range(board_size)))
        for i, row in enumerate(visual_board):
            print(str(i + 1) + " " + " ".join(row))

def parse_args(arglist):
    """ Parse command-line arguments. 
    """
    parser = ArgumentParser()
    parser.add_argument("names", nargs="*", help="enter name")
    return parser.parse_args(arglist)

def coin_toss():
    return random.choice(['heads','tails'])

def gameloop():
    """Main loop to simulate the entire Battleship game."""

    backend = Backend()
    backend.shipPlacement()
    backend.cpuPlacement()
    game = Battleship(backend)

    print("Welcome to Battleship!")
    print("B = Your Ships, X = Hit, O = Miss")

    game.boardVisual()

    while True:
        replace = input("Do you want to replace your ships? (y/n): ")
        if replace == "y":
            backend.shipPlacement()
            game.boardVisual()
            print("Game start!\n")
            break
        elif replace == "n":
            print("Game start!\n")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    args = parse_args(sys.argv[1:])
    print("Captain", *args.names, "!")

    # Main game loop
    while not backend.check_game_over():
        game.boardVisual()
        game.cpuVisual()

        # Player Turn
        valid_shot = False
        while not valid_shot:
            try:
                shot_input = input("Enter coordinates for your shot (e.g. 2,3): ")
                valid_shot = backend.player_shoot(shot_input)
                if not valid_shot:
                    print("Invalid shot or already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid format. Please enter coordinates like 2,3.")
        
        # CPU Turn
        backend.cpu_shoot()

    print("\nGame Over!")
    backend.check_game_over()

if __name__ == "__main__":
    gameloop()
