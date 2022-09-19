num = 0
while num < 1 or num > 10:
    try:
        num = int(input('Inserisci un numero da 1 a 10  '))
    except:
        num = 0
for moltiplicator in range(1, 11):
    print(num*moltiplicator)
