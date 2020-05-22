A = int(input("Entrer la valeur de A = "))
B = int(input("Entrer la valeur de B = "))
Q = 0
R = A

while R >= B:
    R = R - B
    Q = Q+1
print("Quotient entier: "+str(Q))
print("Le reste est: "+str(R))