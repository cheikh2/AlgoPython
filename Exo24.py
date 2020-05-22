A = int(input("Entrer la valeur de A = "))
B = int(input("Entrer la valeur de B = "))

while A!=B:
    if B > A:
        print("Enter la valeur de B plus petit: ")
        B = int(input("Entrer la valeur de B = "))
    if B < A:
        print("Enter la valeur de B plus grand: ")
        B = int(input("Entrer la valeur de B = "))
print("Bravo! vous avez trouver le bon nombre")