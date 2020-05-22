prix = int(input("Entrer le prix du 1° article: "))

somme = 0
while prix != 0:
    somme = somme + prix
    prix= int(input("Entrer le prix de l'article suivant( 0 si Fin):"))
print(" La somme des prix des articles est "+str(somme))