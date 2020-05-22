valeur = int(input("Entrez le 1er nombre : "))

PG = valeur
iPG = 1

for i in range(2, 11):
    valeur = int(input("entrer "+str(i)+"eme valeur"))
    if valeur > PG:
        iPG = i
        PG = valeur
print("le plus grand de ces nombres est:"+ str(PG))
print(" c'était le "+str(iPG)+ " ème nombre saisi")