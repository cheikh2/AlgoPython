hd= int(input("Entrer l'heure de depart = "))
md= int(input("Entrer minutes de depart = "))
ha= int(input("Entrer l'heure d'arrivée = "))
ma= int(input("Entrer minutes d'arrivée = "))

if hd > 0 or hd <  24 or md > 0 or md < 60 and ha > 0 or ha <  24 or ma > 0 or ma < 60:
    if ma > md:
        dha = ha-hd+24
        dma = ma - md
    else:
        dha = ha-hd+24-1
        dma = ma + 60 - md
    print("la durée du vol est : "+str(dha)+" heures et "+str(dma)+" minutes ")

