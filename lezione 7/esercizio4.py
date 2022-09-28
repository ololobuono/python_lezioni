# Creare un dizionario ed eseguire le seguenti operazioni
dizionario = {'table': 'tavolo', 'car': 'auto', 'book': 'libro'}

# Ordinare in funzione delle chiavi

dizionario_ordinato = {}
# estraggo la lista di chiavi e la ordino
chiavi = sorted(dizionario.keys())
# scorro la lista appena realizzata
for chiave in chiavi:
    # individuo il valore corrispondente alla chiave
    valore = dizionario[chiave]
    # aggiungo la coppia chiave/valore al nuovo dizionario
    dizionario_ordinato[chiave] = valore
# mostro il contenuto del nuovo dizionario
print(dizionario_ordinato)

# Ordinare in funzione dei valori

# Verificare se un elemento è presente nel dizionario
print('table presente?', 'table' in dizionario)

# Estrarre chiavi, Estrarre valori
chiavi = list(dizionario.keys())
valori = list(dizionario.values())
print(chiavi)
print(valori)

# Modificare chiavi, Modificare valori

# Aggiungere una nuova coppia chiave/valore
dizionario["onion"] = "cipolla"
print(dizionario)

# Eliminare una chiave da un dizionario
del dizionario["table"]
print(dizionario)

# Eliminare una chiave con pop dal dizionario
dizionario.pop('book',0)
print(dizionario)