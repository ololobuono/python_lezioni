# Creare un dizionario ed eseguire le seguenti operazioni
dizionario = {'table': 'tavolo', 'car': 'auto', 'book': 'libro', 'keys': 'chiavi'}

# Ordinare in funzione delle chiavi
print('Dizionario: ', dizionario)
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
print('Dizionario ordinato per chiavi', dizionario_ordinato)

# Ordinare in funzione dei valori
diz_ordinato_per_valori = {k: v for k, v in sorted(dizionario.items(), key=lambda item: item[1])}
print('Dizionario ordinato per valore: ', diz_ordinato_per_valori)

# Verificare se un elemento è presente nel dizionario
print('Il valore "table" è presente?', 'table' in dizionario)

# Estrarre chiavi, Estrarre valori
chiavi = list(dizionario.keys())
valori = list(dizionario.values())
print('Estraggo le chiavi ', chiavi)
print('Estraggo i valore ', valori)

# Modificare chiavi, Modificare valori

# Aggiungere una nuova coppia chiave/valore
dizionario["onion"] = "cipolla"
print('Aggiungo la chiave onion: ', dizionario)

# Eliminare una chiave da un dizionario
del dizionario["table"]
print('Elimino la chiave table: ', dizionario)

# Eliminare una chiave con pop dal dizionario
dizionario.pop('book',0)

# Eliminare una valore dal dizionario
dizionario = {key:val for key, val in dizionario.items() if val != 'auto'}
print('Elimino il valore auto: ', dizionario)