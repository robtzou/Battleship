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

    def cpu_shoot(self):
        """ CPU takes a shot at player board """
        # Randomly select a coordinate from the available coordinates
        shot = random.choice(self.coordinates)    

        # Check if the shot hits any of the player's ships
        if shot in self.battleship or shot in self.submarine or shot in self.destroyer:
            self.cpu_hits.append(shot)
            print(f"CPU hit at {shot}")
        else:
            self.cpu_shots.append(shot)
            print(f"CPU miss at {shot}")
        
        # Remove the shot from available coordinates
        self.coordinates.remove(shot)
        # Check if any ships are sunk
        self.sunk_ships()

    def player_shoot(self):
        """
        Handles player shot input, validates it, checks for hits, 
        and updates the game state accordingly.

        Side effects:
        - Modifies self.player_shots and self.player_hits lists.
        - Prints result of the shot.
        - Removes the coordinate from self.coordinates if it's a new shot.
        """
        while True:
            try:
                raw_input = input("Captain! Where should we fire?! (Format: Int,Int 1-6) ")
                x_str, y_str = raw_input.strip().split(',')
                x, y = int(x_str), int(y_str)

                if not (1 <= x <= 6 and 1 <= y <= 6):
                    print("Coordinates must be between 1 and 6. Try again.")
                    continue

                shot = (x, y)

                if shot in self.player_shots:
                    print("You've already fired at this location! Try again.")
                    continue

                break
            except ValueError:
                print("Invalid input format. Use two integers like 3,5.")

        # Check if the shot hits any CPU ships
        if shot in self.battleship_cpu or shot in self.submarine_cpu or shot in self.destroyer_cpu:
            self.player_hits.append(shot)
            print(f"Direct hit at {shot}!")
        else:
            print(f"Missed shot at {shot}.")

        self.player_shots.append(shot)
        if shot in self.coordinates:
            self.coordinates.remove(shot)

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

    def shipPlacement(self):
        """Allow player to replace ships within game loop"""
        
        self.battleship = []
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