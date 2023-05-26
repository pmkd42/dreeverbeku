def get_opponent(player, pairings):
    for pairing in pairings:
            if pairing[0] == player:
                return pairing[2]
            elif pairing[2] == player:
                return pairing[0]
    return None