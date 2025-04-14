import random

Xcord = ['a','b','c','d','e','f',]
Ycord = [1,2,3,4,5,6,]

coordinates = [(x, y) for x in Xcord for y in Ycord]

shipPlacement = random.choice(coordinates)

print(shipPlacement)