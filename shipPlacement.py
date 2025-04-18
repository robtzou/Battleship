import random

def shipPlacement():
    
    Xcord = [1,2,3,4,5,6,]
    Ycord = [1,2,3,4,5,6,]
    board_size = len(Xcord)
    coordinates = [(x, y) for x in Xcord for y in Ycord]
    board_lst = [["~" for _ in range(board_size)] for _ in range(board_size)]

    battleship = []
    lenbattleship = 4

    submarine  = []
    lensubmarine = 3

    destroyer  = []
    lendestroyer = 2
    
    while len(battleship) <= lenbattleship:
        placement = random.choice(coordinates)
        if placement[1] + lenbattleship - 1 <= board_size:
            battleship = [(placement[0], placement[1] + i ) for i in range(lenbattleship)]
            coordinates = [coord for coord in coordinates if coord not in battleship]
            break
    while len(submarine) <= lensubmarine:
        placement = random.choice(coordinates)
        if placement[1] + lensubmarine - 1 <= board_size:
            submarine = [(placement[0], placement[1] + i ) for i in range(lensubmarine)]
            coordinates = [coord for coord in coordinates if coord not in submarine]
            break   
    while len(destroyer) <= lendestroyer:
        placement = random.choice(coordinates)
        if placement[1] + lendestroyer - 1 <= board_size:
            destroyer = [(placement[0], placement[1] + i ) for i in range(lendestroyer)]
            return battleship, submarine, destroyer
        
ships = shipPlacement()
print(ships)