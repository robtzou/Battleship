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
        self.coordinates = [(x, y) for x in self.Xcord for y in self.Ycord]

# players boats

        self.battleship = []
        self.lenbattleship = 4
        
        self.submarine  = []
        self.lensubmarine = 3
        
        self.destroyer  = []
        self.lendestroyer = 2

# computers boats

        self.battleship_cpu = []
        self.lenbattleship_cpu = 4
        
        self.submarine_cpu = []
        self.lensubmarine_cpu = 3
        
        self.destroyer_cpu = []
        self.lendestroyer_cpu = 2


# shot history
        self.player_shots = []
        self.cpu_shots = []

# hit markers
        self.player_hits = []
        self.cpu_hits    = []

    def shipPlacement(self):
        """
        Must have an equal chance of placing horizontally or vertically.
        Must not overlap coordinates.
        """
# players

        # Reset ships
        self.battleship = []
        self.submarine = []
        self.destroyer = []
        
        # Refresh available coordinates
        self.coordinates = [(x, y) for x in self.Xcord for y in self.Ycord]
        
        # players
        while len(self.battleship) < self.lenbattleship:
            placement = random.choice(self.coordinates)
            direction = random.choice(['horizontal', 'vertical'])
            
            if direction == 'horizontal' and placement[1] + self.lenbattleship - 1 <= self.board_size:
                self.battleship = [(placement[0], placement[1] + i) for i in range(self.lenbattleship)]
                if all(coord in self.coordinates for coord in self.battleship):
                    self.coordinates = [coord for coord in self.coordinates if coord not in self.battleship]
                    break
            elif direction == 'vertical' and placement[0] + self.lenbattleship - 1 <= self.board_size:
                self.battleship = [(placement[0] + i, placement[1]) for i in range(self.lenbattleship)]
                if all(coord in self.coordinates for coord in self.battleship):
                    self.coordinates = [coord for coord in self.coordinates if coord not in self.battleship]
                    break
            
        while len(self.submarine) < self.lensubmarine:
            placement = random.choice(self.coordinates)
            direction = random.choice(['horizontal', 'vertical'])
            
            if direction == 'horizontal' and placement[1] + self.lensubmarine - 1 <= self.board_size:
                self.submarine = [(placement[0], placement[1] + i) for i in range(self.lensubmarine)]
                if all(coord in self.coordinates for coord in self.submarine):
                    self.coordinates = [coord for coord in self.coordinates if coord not in self.submarine]
                    break
            elif direction == 'vertical' and placement[0] + self.lensubmarine - 1 <= self.board_size:
                self.submarine = [(placement[0] + i, placement[1]) for i in range(self.lensubmarine)]
                if all(coord in self.coordinates for coord in self.submarine):
                    self.coordinates = [coord for coord in self.coordinates if coord not in self.submarine]
                    break
            
        while len(self.destroyer) < self.lendestroyer:
            placement = random.choice(self.coordinates)
            direction = random.choice(['horizontal', 'vertical'])
            
            if direction == 'horizontal' and placement[1] + self.lendestroyer - 1 <= self.board_size:
                self.destroyer = [(placement[0], placement[1] + i) for i in range(self.lendestroyer)]
                if all(coord in self.coordinates for coord in self.destroyer):
                    self.coordinates = [coord for coord in self.coordinates if coord not in self.destroyer]
                    break
            elif direction == 'vertical' and placement[0] + self.lendestroyer - 1 <= self.board_size:
                self.destroyer = [(placement[0] + i, placement[1]) for i in range(self.lendestroyer)]
                if all(coord in self.coordinates for coord in self.destroyer):
                    self.coordinates = [coord for coord in self.coordinates if coord not in self.destroyer]
                    break
                    
        return self.battleship, self.submarine, self.destroyer

    def cpuPlacement(self):
        """
        Must have an equal chance of placing horizontally or vertically.
        Must not overlap coordinates.
        """ 
        # Reset ships
        self.battleship_cpu = []
        self.submarine_cpu = []
        self.destroyer_cpu = []
        
        # Use a fresh set of coordinates for CPU placement
        cpu_coordinates = [(x, y) for x in self.Xcord for y in self.Ycord]
        
        # computers
        while len(self.battleship_cpu) < self.lenbattleship_cpu:
            placement = random.choice(cpu_coordinates)
            direction = random.choice(['horizontal', 'vertical'])
            
            if direction == 'horizontal' and placement[1] + self.lenbattleship_cpu - 1 <= self.board_size:
                self.battleship_cpu = [(placement[0], placement[1] + i) for i in range(self.lenbattleship_cpu)]
                if all(coord in cpu_coordinates for coord in self.battleship_cpu):
                    cpu_coordinates = [coord for coord in cpu_coordinates if coord not in self.battleship_cpu]
                    break
            elif direction == 'vertical' and placement[0] + self.lenbattleship_cpu - 1 <= self.board_size:
                self.battleship_cpu = [(placement[0] + i, placement[1]) for i in range(self.lenbattleship_cpu)]
                if all(coord in cpu_coordinates for coord in self.battleship_cpu):
                    cpu_coordinates = [coord for coord in cpu_coordinates if coord not in self.battleship_cpu]
                    break
            
        while len(self.submarine_cpu) < self.lensubmarine_cpu:
            placement = random.choice(cpu_coordinates)
            direction = random.choice(['horizontal', 'vertical'])
            
            if direction == 'horizontal' and placement[1] + self.lensubmarine_cpu - 1 <= self.board_size:
                self.submarine_cpu = [(placement[0], placement[1] + i) for i in range(self.lensubmarine_cpu)]
                if all(coord in cpu_coordinates for coord in self.submarine_cpu):
                    cpu_coordinates = [coord for coord in cpu_coordinates if coord not in self.submarine_cpu]
                    break
            elif direction == 'vertical' and placement[0] + self.lensubmarine_cpu - 1 <= self.board_size:
                self.submarine_cpu = [(placement[0] + i, placement[1]) for i in range(self.lensubmarine_cpu)]
                if all(coord in cpu_coordinates for coord in self.submarine_cpu):
                    cpu_coordinates = [coord for coord in cpu_coordinates if coord not in self.submarine_cpu]
                    break
            
        while len(self.destroyer_cpu) < self.lendestroyer_cpu:
            placement = random.choice(cpu_coordinates)
            direction = random.choice(['horizontal', 'vertical'])
            
            if direction == 'horizontal' and placement[1] + self.lendestroyer_cpu - 1 <= self.board_size:
                self.destroyer_cpu = [(placement[0], placement[1] + i) for i in range(self.lendestroyer_cpu)]
                if all(coord in cpu_coordinates for coord in self.destroyer_cpu):
                    cpu_coordinates = [coord for coord in cpu_coordinates if coord not in self.destroyer_cpu]
                    break
            elif direction == 'vertical' and placement[0] + self.lendestroyer_cpu - 1 <= self.board_size:
                self.destroyer_cpu = [(placement[0] + i, placement[1]) for i in range(self.lendestroyer_cpu)]
                if all(coord in cpu_coordinates for coord in self.destroyer_cpu):
                    cpu_coordinates = [coord for coord in cpu_coordinates if coord not in self.destroyer_cpu]
                    break
                    
        return self.battleship_cpu, self.submarine_cpu, self.destroyer_cpu

    def replacement(self):

        """Allow player to replace ships within game loop"""
        # Reset ships
        self.battleship = []
        self.submarine = []
        self.destroyer = []
        
        # Replace ships
        self.shipPlacement()

def player_shoot(self, x, y):
    """ Player takes a shot at CPU board """
    # frontend = Battleship()
    # shot = ()
    # tuple_guess = tuple(map(int, .split(",")))
    # if tuple_guess not in self.battleship_cpu or self.submarine_cpu or self.destroyer_cpu:
    pass