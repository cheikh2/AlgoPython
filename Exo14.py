jour = int(input("Entrer un jour : "))
mois = int(input("Entrer un mois : "))
annee = int(input("Entrer une année : "))

if jour<31 and mois<12 and annee%4==0 and annee%100!=0 or annee%400==0:
    print("l'année que vous avez entrer est bissextile")
else:
    print("l’année que vous avez entrer n’ est pas bissextile ou invalide")


