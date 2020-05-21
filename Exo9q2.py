hd= int(input("Entrer l'heure de depart = "))
md= int(input("Entrer minutes de depart = "))
ha= int(input("Entrer l'heure d'arrivée = "))
ma= int(input("Entrer minutes d'arrivée = "))

if ha > hd:
    if ma > md:
        dha = ha-hd
        dma = ma - md
    else:
        dha = ha-hd-1
        dma = ma + 60 - md
else:
    if ma > md:
        dha = ha-hd+24
        dma = ma - md
    else:
        dha = ha-hd+24-1
        dma = ma + 60 - md
        
print("la durée du vol est : "+str(dha)+" heures et "+str(dma)+" minutes ")

