import random

def coin():
    return random.choice([0,1])

class Backend:
    """
    Setup the game to be played.
    Place boats.
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
            