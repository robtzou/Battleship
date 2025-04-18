def win(ships):
    for ship in ships:
        if not all(ship["parts"]):
            return False
    return True
