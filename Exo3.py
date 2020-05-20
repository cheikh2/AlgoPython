def main():
    r1= int(input("Entrer la valeur de r1 = "))
    r2= int(input("Entrer la valeur de r2 = "))
    r3= int(input("Entrer la valeur de r3 = "))
    choix= int(input("Entrer la valeur de choix = "))

    Rser = r1+r2+r3
    Rpar = (r1*r2*r3) / (r1*r2+r1*r3+r2*r3)

    if choix == 1:
        print("a resistance equivalente de r1 ,r2 et r3 en serie est: "+ str(Rser))

    if choix == 2:
        print("a resistance equivalente de r1 ,r2 et r3 en serie est: "+ str(Rpar))

if __name__ == "__main__":
    main()