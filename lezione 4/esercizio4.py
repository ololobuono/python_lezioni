try:
    worked_hours = int(input('Ore lavorate: '))
except:
    print('Hai inserito un valore non valido. Inserisci un numero intero')
    exit()
hourly_rate = 10
work_hours = 40
if worked_hours <= work_hours:
    total_pay = worked_hours * hourly_rate
else:
    total_pay = (work_hours * hourly_rate) + ((worked_hours - work_hours) * (hourly_rate * 1.5))
print('Paga totale: ' + str(total_pay))