
from datetime import time, datetime
from datetime import timedelta
from time import sleep
import winsound

print('Entrez votre miniteur')

heure = int(input('H:'))
minute = int(input('MIN:'))
seconde = int(input('S:'))

temps = time(heure, minute, seconde)

maintenant = datetime.now()
duree = timedelta(hours= heure, minutes= minute, seconds= seconde)
futur = maintenant + duree

fin = 0

print('Début du minuteur',futur)

while fin != 1:
    
    if datetime.now() >= futur:
        winsound.PlaySound("SystemHand", winsound.SND_LOOP)
        print(futur)
        fin += 1
    sleep(1)