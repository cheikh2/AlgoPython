a= int(input("Entrer la valeur de a = "))
operateur= str(input("Entrer l'operateur = "))
b= int(input("Entrer la valeur de b = "))

if operateur =='+':
    print("La somme est: "+str(a+b))
if operateur =='-':
    print("Le resultat est: "+str(a-b))
if operateur =='*':
    print("Le resultat est: "+str(a*b))
if operateur =='/' and b!=0:
    print("Le resultat est: "+str(a/b))
else:
    print("Opération impossible")
