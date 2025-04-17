import random

Xcord = ['a','b','c','d','e','f',]
Ycord = [1,2,3,4,5,6,]

coordinates = [(x, y) for x in Xcord for y in Ycord]
shipPlacement = random.choice(coordinates)

battleship = []
destroyer  = []
submarine  = []

board_size = len(Xcord)
board_lst = [["~" for _ in range(board_size)] for _ in range(board_size)]

for i in range(3):
    board[2][1 + i] = "*"


