# In una sessione di esami gli studenti hanno preso i seguenti voti: 29, 18, 18, 25, 28, 27, 19, 30, 20
# Calcolare e mostrare la media aritmetica, la moda e la mediana

# importo il modulo statistics
import statistics
sessione = (29, 18, 18, 25, 28, 27, 19, 30, 20)

print('media: ', statistics.mean(sessione))
print('moda: ', statistics.mode(sessione))
print('mediana: ', statistics.median(sessione))