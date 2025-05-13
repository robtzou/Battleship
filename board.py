import random

class Backend:
    """Setup the game to be played. The ship size and the ship placement for CPU
    player and human player.


    Attributes:
        board_size(int): 6 by 6 board.
        Xcords(list): x coordinates of board game
        Ycords(list): y coordinates of board game
        coordinates(list of tuple): pairs of x and y coordintes
        
        battleship_cpu(list): coordinates of ship of CPU
        player_shots)(list): player shots on CPU ship
        cpu_shots(list): shots on the human player
        
        player_hits(list): all the coordinates
        cpu_hits(list): all the coordinates
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

    def cpu_shoot(self):
        """ CPU takes a shot at player board """
        if not self.coordinates:
            print("CPU has no more coordinates to shoot.")
            return
        
        # Randomly select a coordinate from the available coordinates
        shot = random.choice(list(self.coordinates))
        self.coordinates.discard(shot)    

        # Check if the shot hits any of the player's ships
        if shot in self.battleship or shot in self.submarine or shot in self.destroyer:
            self.cpu_hits.append(shot)
            print(f"CPU hit at {shot}")
        else:
            self.cpu_shots.append(shot)
            print(f"CPU miss at {shot}")
    
    def player_shoot(self, player_guess):
        """
        Takes a guess from the player, validates it, checks for hits, 
        and updates the game state accordingly.

        Parameters:
        - player_guess: str in format "x,y"

        Side effects:
        - Modifies self.player_shots and self.player_hits.
        - Prints result of the shot.
        - Removes coordinate from self.coordinates if it's a new shot.
        """
        try:
            x_str, y_str = player_guess.strip().split(',')
            x, y = int(x_str), int(y_str)

            if not (1 <= x <= 6 and 1 <= y <= 6):
                print("Coordinates must be between 1 and 6.")
                return False  # Invalid input range

            shot = (x, y)

            if shot in self.player_shots:
                print("You've already fired at this location!")
                return False  # previous shot

        except ValueError:
            print("Invalid input format. Use two integers like 3,5.")
            return False  # Bad format

        # Check for hit
        if shot in self.battleship_cpu or shot in self.submarine_cpu or shot in self.destroyer_cpu:
            self.player_hits.append(shot)
            print(f"Direct hit at {shot}!")
        else:
            print(f"Missed shot at {shot}.")

        self.player_shots.append(shot)
        self.coordinates.discard(shot)  # Use discard to avoid KeyError if already gone
        return True  # Shot successfully processed

    def sunk_ships(self):
        """Displays game progress"""
        
        while True:
            if self.player_hits == self.battleship_cpu:
                print("CPU: You sunk my Battleship! ")
            if self.player_hits == self.submarine_cpu:
                print("CPU: You sunk my Submarine! ")
            if self.player_hits == self.destroyer_cpu:
                print("CPU: You sunk my Destroyer! ")
            if self.player_hits == self.battleship:
                print("Your Battleship has been sunk..")
            if self.player_hits == self.submarine:
                print("Your Submarine has been sunk..")
            if self.player_hits == self.destroyer:
                print("Your Destroyer has been sunk..")
            break

    def check_game_over(self):
        """Return True if either the player or CPU has no ships left afloat."""
    
        player_sunk = all(coord in self.cpu_hits for ship in [self.battleship, self.submarine, self.destroyer] for coord in ship)
        cpu_sunk = all(coord in self.player_hits for ship in [self.battleship_cpu, self.submarine_cpu,
                                                               self.destroyer_cpu] for coord in ship)
        if player_sunk:
            return "All of your ships are sunk! Better luck next time!"
        elif cpu_sunk:
            return "You won! Great job Captain!"   
        
        return player_sunk or cpu_sunk
    
    def place_ship(self, length):

        """ 
        Author: Robert Tzou, Technique: List / Set Comprehension

        Places the ships within the limits of the board.
        Determines horizontal or vertical placement based on random choice.

        Args:

        Returns: 

        Side effects: Populates a list with selected coordinates.


        """        
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
        
        self.battleship =[]
        self.submarine = []
        self.destroyer = []
        
        self.battleship = self.place_ship(self.lenbattleship)
        self.submarine  = self.place_ship(self.lensubmarine)
        self.destroyer  = self.place_ship(self.lendestroyer)

    def cpuPlacement(self):
        """Calls upon place_ship function to place CPU ships"""

        self.battleship_cpu = []
        self.submarine_cpu  = []
        self.destroyer_cpu  = []

        self.battleship_cpu = self.place_ship(self.lenbattleship)
        self.submarine_cpu  = self.place_ship(self.lensubmarine)
        self.destroyer_cpu  = self.place_ship(self.lendestroyer)