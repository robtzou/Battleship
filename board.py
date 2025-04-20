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
        self.board_lst = [["~" for _ in range(self.board_size)] for _ in range(self.board_size)]

        self.battleship = []
        self.lenbattleship = 4
        
        self.submarine  = []
        self.lensubmarine = 3
        
        self.destroyer  = []
        self.lendestroyer = 2
        
    def shipPlacement(self):
        """
        Must have an equal chance of placing horizontally or vertically.
        Must not overlap coordinates.
        """
        coin
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