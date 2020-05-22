jour= int(input("Entrer le jour : "))
mois= int(input("Entrer le mois : "))
annee= int(input("Entrer l'annee : "))

if jour > 0 and jour <= 31 and mois > 0 and mois <= 12 and annee>1900 and annee < 2999:
    print("la date: "+str(jour)+"/"+str(mois)+"/"+str(annee)+" est valide")
else:
    print("la date: "+str(jour)+"/"+str(mois)+"/"+str(annee)+" est invalide")
    
        