from random import randrange
list = [randrange(18, 30),randrange(18, 30),randrange(18, 30),randrange(18, 30),randrange(18, 30),randrange(18, 30),randrange(18, 30)]
# Stampo la lista
print('Lista di voti: ', list)
lower = 31
for num in list:
    if num < lower:
        lower = num
print('Il voto più basso è ' + str(lower))
