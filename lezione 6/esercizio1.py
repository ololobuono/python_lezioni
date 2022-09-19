#Creo una lista di oggetti
lista = ["3","14","3","8",'test',"3","7"]
# Stampo la lista
print('Lista: ', lista)
tupla = ('Tupla Tupla Tupla', 'l\ho inventato ioooo', '4', '100')
# Stampo la Tupla
print('Tupla: ', tupla)
count_el = 0
for i in lista :
    count_el = count_el + 1
print('Nella lista ci sono ' + str(count_el) + ' elementi')
count_el = 0
for i in tupla :
    count_el = count_el + 1
print('Nella tupla ci sono ' + str(count_el) + ' elementi')