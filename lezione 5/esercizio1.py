#Creo una lista di oggetti
lista = ["3","14","3","8",'test',"3","7"]
# Stampo la lista
print('Lista: ', lista)
# stampo il secondo elemento della lista
print('Secondo Elemento: ', lista[1])
# Sostituisco il 3 valore della lista
lista[2] = 'sostituito'
# Stampo la nuova lista
print('Lista: ', lista)
# Stampo i primi 3 elementi della lista
print('Primi 3 elementi: ', lista[:3])
# Rimuovere il 2 elemento della lista
del lista[1]
# ristampo la lista
print('Lista: ', lista)
# Conto quante volte un elemento è presente nella lista
needle = input('Digita l\'elemento che vuoi cercare: ')
num_found = lista.count(str(needle))
print('L\'elemento ' + str(needle) + ' è stato trovato ' + str(num_found) + ' volte')

