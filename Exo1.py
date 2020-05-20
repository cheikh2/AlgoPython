def main():
     A= int(input("Entrer la valeur de A = "))
     B = int(input("Entrer la valeur de B = "))

     quotien = A//B 
     quotienReel = A/B
     reste = A%B

     print("Le quotien de A et B est: " + str(quotien))
     print("Le quotien reel de A et B est: " + str(quotienReel))
     print("Le reste de A et B est: " + str(reste))

if __name__ == "__main__":
    main()