### jacklyn 

import board

def sunkenships():
    """
    This function prints a message indicating that the ship has sunk.
    """

    if len(board.battleship) == 0:
        print("You have sunk their battleship!")
    if len(board.destroyer) == 0:
        print("You have sunk their destroyer!")
    if len(board.submarine) == 0:
        print("You have sunk their submarine!")
    if len(board.battleship) == 0 and len(board.destroyer) == 0 and len(board.submarine) == 0:
        print("You have sunk all their ships!")
