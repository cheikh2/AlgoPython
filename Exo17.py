a = int(input("Entrer la valeur de A = "))
b = int(input("Entrer la valeur de B = "))

if a < 0 or b < 0:
    e = a
    d = b
    Pgcd  = 0
    resu = 0
while a != b:
     if b>a:
         c=a
         a=b
         b=c
     resu = a-b
     a = b
     b = resu
     pgcd = a

print("le PGCD de A et B est : "+ str(pgcd))