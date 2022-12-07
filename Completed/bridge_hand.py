def bridge_hand_shape(hand):
    cards = [b for a, b in hand]
    spades = cards.count('spades')
    hearts = cards.count('hearts')
    diamonds = cards.count('diamonds')
    cardst = cards.count('clubs')
    return [spades, hearts, diamonds, cardst]