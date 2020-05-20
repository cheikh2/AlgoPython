def main():
    montant= int(input("Entrer le montant à décomposer =  "))

    if montant > 0:
        billet20 = montant / 20
        billet10 = (montant % 20)/10
        billet5 = ((montant%20)%10)/5
        piece2 = (((montant%20)%10)%5)/2
        piece1 = ((((montant%20)%10)%5)%2)
		

    print("Le montant "+str(montant)+" à "+str(billet20)+" billet(s) de 20€")
    print(str(billet10)+" billet(s) de 10€")
    print(str(billet5)+" billet(s) de 5€")
    print(str(piece2)+" piece(s) de 2€")
    print(str(piece1)+" piece(s) de 1€")
    

if __name__ == "__main__":
    main()