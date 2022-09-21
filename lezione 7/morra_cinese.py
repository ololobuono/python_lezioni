# Gioca alla morra cinese indicando le due mosse:
# Move: 1 per Carta, 2 per Forbice, 3 per Pietra
# Ritorna 1 se vince la mossa 1 o 2 se vince la mossa 3, 0 se pareggio
def play(move1, move2):
    if move1 == 1 :
        if move2 == 1:
            return 0
        elif move2 == 2:
            return 2
        elif move2 == 3:
            return 1
    if move1 == 2 :
        if move2 == 1:
            return 1
        elif move2 == 2:
            return 0
        elif move2 == 3:
            return 2
    if move1 == 3 :
        if move2 == 1:
            return 2
        elif move2 == 2:
            return 1
        elif move2 == 3:
            return 0
def getMoveDesc(move):
    if move == 1:
        return 'Carta'
    elif move == 2:
        return 'Forbice'
    elif move == 3:
        return 'Pietra'
    else:
        return ''
