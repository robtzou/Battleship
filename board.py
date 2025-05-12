import random

class Backend:
    """
    Setup the game to be played.
    Place boats.
    """
    
    def __init__(self):
        
        self.Xcord = [1,2,3,4,5,6,]
        self.Ycord = [1,2,3,4,5,6,]
        self.board_size = 6
        self.coordinates = set([(x, y) for x in self.Xcord for y in self.Ycord])
        

# players boats
        self.battleship   = []
        self.lenbattleship= 4
        
        self.submarine    = []
        self.lensubmarine = 3
        
        self.destroyer    = []
        self.lendestroyer = 2

# computers boats
        self.battleship_cpu = []
        self.submarine_cpu  = []
        self.destroyer_cpu  = []
        
# shot history
        self.player_shots = []
        self.cpu_shots = []

# hit markers
        self.player_hits = []
        self.cpu_hits    = []

    def place_ship(self, length):
        while True:
            placement = random.choice(list(self.coordinates))
            direction = random.choice(['horizontal', 'vertical'])

            if direction == 'horizontal' and placement[1] + length - 1 <= self.board_size:
                ship = [(placement[0], placement[1] + i) for i in range(length)]
            elif direction == 'vertical' and placement[0] + length - 1 <= self.board_size:
                ship = [(placement[0] + i, placement[1]) for i in range(length)]
            else:
                continue

            if all(coord in self.coordinates for coord in ship):
                self.coordinates.difference_update(ship)
                return ship

    def shipPlacement(self):

        """Allow player to replace ships within game loop"""
        
        self.battleship = []
        self.submarine = []
        self.destroyer = []
        
        self.battleship = self.place_ship(self.lenbattleship)
        self.submarine  = self.place_ship(self.lensubmarine)
        self.destroyer  = self.place_ship(self.lendestroyer)

    def cpuPlacement(self):
        
        self.battleship_cpu = []
        self.submarine_cpu  = []
        self.destroyer_cpu  = []

        self.battleship_cpu = self.place_ship(self.lenbattleship)
        self.submarine_cpu  = self.place_ship(self.lensubmarine)
        self.destroyer_cpu  = self.place_ship(self.lendestroyer)

def player_shoot(self, x, y):
    """ Player takes a shot at CPU board """
    # frontend = Battleship()
    # shot = ()
    # tuple_guess = tuple(map(int, .split(",")))
    # if tuple_guess not in self.battleship_cpu or self.submarine_cpu or self.destroyer_cpu:
    pass