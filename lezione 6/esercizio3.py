from random import randrange
# random da 1 a 100
num_rand = randrange(1, 101)
num = 0
contatore = 0
while num != num_rand:
    try:
        num = int(input('Inserisci un numero da 1 a 100 (scrivi 999 per uscire): '))
    except:
        num = 0
    contatore = contatore + 1
    if num == 999:
        print('Bye! ')
        break
    elif num < 1 or num > 100:
        continue
    elif num == num_rand:
        print('Complimenti hai vinto in ' + str(contatore) + ' tentativi')
    elif num > num_rand:
        print('Il numero scelto è troppo grande ')
    elif num < num_rand:
        print('Il numero scelto è troppo piccolo ')
