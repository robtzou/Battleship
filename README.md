# Battleship
Final Project repo for Battleship game.

Group Members: Robert Tzou, Jacklyn Dang, Oswalt Vasquez , Christopher Okure.

# How to run program

Open your terminal, run the following: 'git clone https://github.com/robtzou/Battleship'

Make sure the cloned folder is in your wording directory. e.g. pwd -> Downloads/Battleship

To run the program type: python3 main.py [name]


# How to play
First, you start by putting your name. Then the terminal will give you options for your ship placement. You will input y or n. If you say yes, the program will continue with the game. If you put in the program will give you other placements of the ships until you find what you preferred. Then you will input a x coordinate and a y coordinate. It will say if you missed or hit a ship. If you destroy an entire ship, it will say the name of the ship that you have sunk. Until you have sunk all three ships, it will display who wins at the end of the game.

# Attribution Table

| Method / Function | Author Name | Techniques Demonstrated |
|-------------------|-------------|-------------------------|
| place_ships | Robert | Set Operations / Sequence Unpacking |
| boardVisual / cpuVisual | Robert | List Comprehension |
| parse_args  | Oswalt Vasquez | ArgumentParser class  |
|cpu_shot     | Oswalt Vasquez | Coditional expression |
| check_game_over | Christopher Okure | set operations |
| gameloop | Christopher Okure | Composition of two custom classes |
|sunken_ships|Jacklyn Dang|Generator expression|
|Player_shoot|Jacklyn Dang|conditional expression|


# Annotated Bibliography

WikiHow. (n.d.). How to play Battleship. https://www.wikihow.com/Play-Battleship

Stack Overflow user 37084246. (2016, May 6). Printing using list comprehension [Online forum post]. 

Stack Overflow. https://stackoverflow.com/questions/37084246/printing-using-list-comprehension
