a = int(input("Entrer la valeur de A = "))
b = int(input("Entrer la valeur de B = "))

c=a
d=b

while a!=b:
    if a>b:
        b = b+d
    else:
        a = a+c
print(" le PPCM de A et B est "+str(a))