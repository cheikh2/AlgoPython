hd= int(input("Entrer l'heure de depart = "))
md= int(input("Entrer minutes de depart = "))
ha= int(input("Entrer l'heure d'arrivée = "))
ma= int(input("Entrer minutes d'arrivée = "))

dma = (ha*60+ma)-(hd*60+md)
dha = dma/60

print("La durée du vol est: "+str(dha))

