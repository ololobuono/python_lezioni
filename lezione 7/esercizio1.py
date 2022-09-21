from random import randrange
import morra_cinese
players = 0
player1 = 0
player2 = 0
while players != 1 and players != 2 :
    try:
        players = int(input('Indica il numero di giocatori digitando 1 o 2 (scrivi 999 per uscire): '))
    except:
        players = 0
    if players == 999:
        print('Bye! ')
        break
    if players == 1:
        while player1 != 1 and player1 != 2 and player1 != 3:
            try:
                player1 = int(input('Giocatore 1 -> Digita 1 per Carta, 2 per Forbice, 3 per Pietra: '))
            except:
                player1 = 0
            print('Hai scelto ' + morra_cinese.getMoveDesc(player1))
            # Scelgo la mossa del PC da 1 a 3 (1 per Carta, 2 per Forbice, 3 per Pietra
            pc = randrange(1, 4)
            print('Il pc ha scelto ' + morra_cinese.getMoveDesc(pc))
            who_wins = morra_cinese.play(player1, pc)
            if who_wins == 0:
                print('Male ma non malissimo, hai pareggiato')
            elif who_wins == 1:
                print('Complimenti, hai vinto')
            else:
                print('Mi dispiace, sei scarso, hai perso')
    elif players == 2:
        while player1 != 1 and player1 != 2 and player1 != 3:
            try:
                player1 = int(input('Giocatore 1 -> Digita senza farti vedere 1 per Carta, 2 per Forbice, 3 per Pietra: '))
            except:
                player1 = 0
        while player2 != 1 and player2 != 2 and player2 != 3:
            try:
                player2 = int(input('Giocatore 2 -> Digita senza farti vedere 1 per Carta, 2 per Forbice, 3 per Pietra: '))
            except:
                player2 = 0
        print('Il giocatore 1 ha scelto ' + morra_cinese.getMoveDesc(player1))
        print('Il giocatore 2 ha scelto ' + morra_cinese.getMoveDesc(player2))
        who_wins = morra_cinese.play(player1, player2)
        if who_wins == 0:
            print('Male ma non malissimo, avete pareggiato')
        elif who_wins == 1:
            print('Complimenti, ha vinto il giocatore 1')
        else:
            print('Complimenti, ha vinto il giocatore 2')
