valeur= int(input("Entrer la valeur : "))
somme = 0

for i in range(1, valeur):
    if valeur%i==0:
        somme = somme + i
if somme==valeur:
    print("le nombre :"+str(valeur)+" est parfait")
else:
    print("le nombre :"+str(valeur)+" n'est pas parfait")