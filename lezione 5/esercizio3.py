
first_number = float(input('Inserisci un numero: '))
second_number = float(input('Inserisci un altro numero: '))
operator = input('Indica un operatore tra: +, -, *, / :')
# Definisco le funzioni della calcolatrice
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def multi(a, b):
    return a * b
def div(a, b):
    if (b != 0) :
        return a / b
    else:
        return 'Impossibile dividere per 0'
if (operator == '+'):
    print('Risultato: ', add(first_number, second_number))
elif (operator == '-'):
    print('Risultato: ', sub(first_number, second_number))
elif (operator == '*'):
    print('Risultato: ', multi(first_number, second_number))
elif (operator == '/'):
    print('Risultato: ', div(first_number, second_number))