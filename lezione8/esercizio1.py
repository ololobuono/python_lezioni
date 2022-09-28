# Indovina il numero misterioso

# Creare un ambiente virtuale chiamato laboratorio dove far
# Realizzare un piccolo gioco “numero_misterioso”

# 1. Importare la libreria random
from random import randrange
# 2. Far scegliere all’utente la lingua (IT on ENG)
lang = int(input('Scegli la lingua IT (1). Choose language ENG (2): '))
guessed_it = 0
wrong_it = 0
while guessed_it < 10:
    # 3. Generare un numero misteioso da 1 a 10
    mysterious_num = randrange(1, 11)
    # 4. Chiedere all’utente se il numero misterioso è <= a 5 o >5
    if lang == 1:
        choosen = int(input('Secondo te il numero misterioso è minore uguale a 5 (1) o maggiore di 5 (2)? '))
    else:
        choosen = int(input('According to you, the mysterious number is less or equal than 5 (1) or greather than 5 (2)? '))
    # 5. Comunicare all’utente il risultato.
    if (choosen == 1 and mysterious_num <= 5) or (choosen == 2 and mysterious_num > 5):
        guessed_it += 1
        if lang == 1:
            print('Complimenti hai indovinato')
        else:
            print('Congrats you guessed it')
    else:
        wrong_it += 1
        if lang == 1:
            print('Mi dispiace, non hai indovinato')
        else:
            print('I\'m sorry, you don\'t guessed it')
    if wrong_it >= 10:
        if lang == 1:
            print('Mi dispiace, hai sbagliato 10 volte. Gioco finito.')
        else:
            print('I\'m sorry, you were wrong 10 times. Game Over.')
        break
if guessed_it >= 10:
    if lang == 1:
        print('Complimenti hai vinto. Hai indovinato 10 volte')
    else:
        print('You Win. You guessed it 10 times')
# 6. Tenere conto dei risultati; l’utente vince se indovina 10 volte
# prima di sbagliare 10 volte