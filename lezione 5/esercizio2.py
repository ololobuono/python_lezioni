print ('----------funzione type()---------')
#Creo una lista di oggetti
lista = ["3","14","3","8",'test',"3","7"]
# Stampo la lista
print('Lista: ', lista)
# Stampo il tipo di variabile della lista tramite la funzione type
print('Tipo variabile lista: ', type(lista))
stringa = 'Prova text'
print('Testo: ', lista)
# Stampo il tipo di variabile della stringa tramite la funzione type
print('Tipo variabile stringa: ', type(stringa))
# Uso la funzione map (è una funzione iteratrice). Esegue la funzione indicata
# nel primo argomento per ogni elemento della variabile lista. In questo caso raddoppio
# i numeri della lista con una funzione definita da me che raddoppia un numero
print ('----------funzione map()---------')
def double(n):
    return n + n
lista = [1, 5, 13, 22]
print('Lista da raddoppiare: ',  lista)
result = map(double, lista)
print('Lista Raddoppiata: ', list(result))
print('----------funzione exec()---------')
# Eseguo lo scrypt scritto in una stringa
executable = 'a = 7\nb=8\nprint("Risultato Moltiplicazione =", a*b)'
print('Stringa da eseguire: ' + executable)
exec(executable)


