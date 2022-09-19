from random import randrange
# Voti da 18 a 30
list = [randrange(18, 31),randrange(18, 31),randrange(18, 31),randrange(18, 31),randrange(18, 31),randrange(18, 31),randrange(18, 31)]
# Stampo la lista
print('Lista di voti: ', list)
lower = 31
higher = 0
for num in list:
    if num < lower:
        lower = num
    if num > higher:
        higher = num
print('Il voto più basso è ' + str(lower))
print('Il voto più alto è ' + str(higher))
