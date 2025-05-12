from board import Backend
from argparse import ArgumentParser

""" 
    A one player version of speed-battleship where 
    the opponent is a computer.
    One Battleship - 4
    One Submarine  - 3
    One Destroyer  - 2
"""

class Battleship:
    """Displays the game"""
    def __init__(self, backend_instance):
        self.backend_instance = backend_instance
        
    def boardVisual(self):
        """Player board"""
        board_size = 6

        # New board
        visual_board = [["~" for _ in range(board_size)] for _ in range(board_size)]

        player_ships = (
        self.backend_instance.battleship +
        self.backend_instance.submarine +
        self.backend_instance.destroyer
        )

        # Place ships
        for x, y in player_ships:
            visual_board[x - 1][y - 1] = "B"
            
        # Mark CPU hits on player board
        for x, y in self.backend_instance.cpu_hits:
            visual_board[x - 1][y - 1] = "X"
            
        # Mark CPU misses on player board
        for x, y in self.backend_instance.cpu_shots:
            if (x, y) not in self.backend_instance.cpu_hits:
                visual_board[x - 1][y - 1] = "O"

        # Display board
        print("\nYour Board:")
        print("  " + " ".join(str(i + 1) for i in range(board_size)))
        for i, row in enumerate(visual_board):
            print(str(i + 1) + " " + " ".join(row))

    def cpuVisual(self):
        board_size = 6

        visual_board = [["~" for _ in range(board_size)] for _ in range(board_size)]
        
        # We don't show CPU ships, only hits and misses
        
        # Mark player hits
        for x, y in self.backend_instance.player_hits:
            visual_board[x - 1][y - 1] = "X"
            
        # Mark player misses
        for x, y in self.backend_instance.player_shots:
            if (x, y) not in self.backend_instance.player_hits:
                visual_board[x - 1][y - 1] = "O"
        
        # Display cpu board
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

def gameloop():
    """ Make a mainloop that iterates to simulate the entire game. """
    
    backend = Backend()
    backend.shipPlacement()
    backend.cpuPlacement()
    game = Battleship(backend)

# welcome user and start the game
    print("Welcome to Battleship!")
    print("B = Your Ships, X = Hit, O = Miss")

    game.boardVisual()
    while True:
        replace = input("Do you want to replace your ships? (y/n): ")
        if not replace == "n":
                backend.shipPlacement()
                game.boardVisual()
        else:
            print("Game start!")
            break
    
    # Game sequence loop
    game_over = False
    while not game_over:
        game.boardVisual()
        game.cpuVisual()

        # Player turn
        try:
            args = parse_args(sys.argv[1:])
            coordinate_guess = input(f"\n Captain {args.names}! Enter coordinates for your shot! ex. (1,1): ")
            
            break


        except ValueError:
            print("Please enter a valid coordinate.")

if __name__ == "__main__":
    gameloop()