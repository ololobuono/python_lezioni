from random import randrange
# Voti da 18 a 30
list = [randrange(18, 31),randrange(18, 31),randrange(18, 31),randrange(18, 31),randrange(18, 31),randrange(18, 31),randrange(18, 31)]
# Stampo la lista
print('Lista di voti: ', list)
lower = 31
for num in list:
    if num < lower:
        lower = num
print('Il voto più basso è ' + str(lower))
