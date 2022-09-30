#Creare un set con gli elementi dell’ insieme delle note musicali
note_musicali = {'do', 're', 'mi', 'fa', 'sol', 'la', 'si'}
print('Set note musicali: ', note_musicali)

#Creare un set con gli elementi dell’ insieme articoli determinativi della lingua italiana.
art_determinativi = {'il', 'lo', 'la', 'i', 'gli', 'le'}
print('Set note musicali: ', art_determinativi)

#Mostrare l’unione dei due set
print('Unione= ', note_musicali | art_determinativi)

#Mostrare l’ intersezione tra i due set
print('Intersezione= ', note_musicali & art_determinativi)

#Mostrare la differenza tra i due set
print('Differenza note - art= ', note_musicali - art_determinativi)
print('Differenza art - note= ', art_determinativi -note_musicali)

#Mostrare la intersezione simmetrica tra i due set
print('Intersezione simmetrica= ', note_musicali ^ art_determinativi)

