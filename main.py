""" A one player version of speed-battleship where 
    the opponent is a computer.
    One Battleship - 4
    One Submarine  - 3
    One Destroyer  - 2
"""
import random

class Backend:
    """
    Setup the game to be played.
    Place boats allow the option to replace them until satisfactory.
    """
    def __init__(self):
        
        self.Xcord = [1,2,3,4,5,6,]
        self.Ycord = [1,2,3,4,5,6,]
        self.board_size = 6
        self.coordinates = [(x, y) for x in self.Xcord for y in self.Ycord]

    # players
        self.battleship = []
        self.lenbattleship = 4
        
        self.submarine  = []
        self.lensubmarine = 3
        
        self.destroyer  = []
        self.lendestroyer = 2

    # computers
        self.battleship_cpu = []
        self.lenbattleship_cpu = 4
        
        self.submarine_cpu = []
        self.lensubmarine_cpu = 3
        
        self.destroyer_cpu = []
        self.lendestroyer_cpu = 2
    def shipPlacement(self):
        """
        Must have an equal chance of placing horizontally or vertically.
        Must not overlap coordinates.
        """
    # players
        while len(self.battleship) <= self.lenbattleship:
            placement = random.choice(self.coordinates)
            if placement[1] + self.lenbattleship - 1 <= self.board_size:
                self.battleship = [(placement[0], placement[1] + i) for i in range(self.lenbattleship)]
                self.coordinates = [coord for coord in self.coordinates if coord not in self.battleship]
                break
            
        while len(self.submarine) <= self.lensubmarine:
            placement = random.choice(self.coordinates)
            if placement[1] + self.lensubmarine - 1 <= self.board_size:
                self.submarine = [(placement[0], placement[1] + i ) for i in range(self.lensubmarine)]
                self.coordinates = [coord for coord in self.coordinates if coord not in self.submarine]
                break
            
        while len(self.destroyer) <= self.lendestroyer:
            placement = random.choice(self.coordinates)
            if placement[1] + self.lendestroyer - 1 <= self.board_size:
                self.destroyer = [(placement[0], placement[1] + i ) for i in range(self.lendestroyer)]
                return self.battleship, self.submarine, self.destroyer
    def cpuPlacement(self):
        """
        Must have an equal chance of placing horizontally or vertically.
        Must not overlap coordinates.
        """ 
    # computers

        while len(self.battleship_cpu) <= self.lenbattleship_cpu:
            placement = random.choice(self.coordinates)
            if placement[1] + self.lenbattleship_cpu - 1 <= self.board_size:
                self.battleship_cpu = [(placement[0], placement[1] + i) for i in range(self.lenbattleship_cpu)]
                self.coordinates = [coord for coord in self.coordinates if coord not in self.battleship_cpu]
                break
            
        while len(self.submarine_cpu) <= self.lensubmarine_cpu:
            placement = random.choice(self.coordinates)
            if placement[1] + self.lensubmarine_cpu - 1 <= self.board_size:
                self.submarine_cpu = [(placement[0], placement[1] + i ) for i in range(self.lensubmarine_cpu)]
                self.coordinates = [coord for coord in self.coordinates if coord not in self.submarine_cpu]
                break
            
        while len(self.destroyer_cpu) <= self.lendestroyer_cpu:
            placement = random.choice(self.coordinates)
            if placement[1] + self.lendestroyer_cpu - 1 <= self.board_size:
                self.destroyer_cpu = [(placement[0], placement[1] + i ) for i in range(self.lendestroyer_cpu)]
                return self.battleship_cpu, self.submarine_cpu, self.destroyer_cpu
    def replacement(self):
        """Allow player to replace ships within game loop"""
        ships = self.battleship + self.submarine + self.destroyer
        ships.clear()
        # instance of backend
        backend=Backend()
        # replace ships
        backend.shipPlacement()

class Battleship:

    def __init__(self, backend_instance):
        self.backend_instance = backend_instance

    def boardVisual(self):
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

        # Display board
        print("  " + " ".join(str(i + 1) for i in range(board_size)))
        for i, row in enumerate(visual_board):
            print(str(i + 1) + " " + " ".join(row))

        return "Your Board"

    def cpuVisual(self):
        board_size = 6

        visual_board = [["~" for _ in range(board_size)] for _ in range(board_size)]
        
        cpu_ships = (
        self.backend_instance.battleship_cpu +
        self.backend_instance.submarine_cpu +
        self.backend_instance.destroyer_cpu
    )
    
        for x, y in cpu_ships:
            visual_board[x - 1][y - 1] = "0" # change to ~ for demo
        
        # Display cpu board
        print("  " + " ".join(str(i + 1) for i in range(board_size)))
        for i, row in enumerate(visual_board):
            print(str(i + 1) + " " + " ".join(row))
        return "CPU Board"

def gameloop(self):
    # instance of backend
    backend = Backend()
    # access backend placement coordinates
    player_ships = backend.shipPlacement()
    cpu_ships = backend.cpuPlacement()
    # tell these two classes to communicate
    battleship = Battleship(backend)
    # literal display
    print("\nCPU Board")
    cpu_board = battleship.cpuVisual()
    print("\nYour Board")
    board = battleship.boardVisual()    


if __name__ == "__main__":
    # instance of backend
    backend = Backend()
    # access backend placement coordinates
    player_ships = backend.shipPlacement()
    cpu_ships = backend.cpuPlacement()
    # tell these two classes to communicate
    battleship = Battleship(backend)
    # literal display
    print("\nCPU Board")
    cpu_board = battleship.cpuVisual()
    print("\nYour Board")
    board = battleship.boardVisual()
