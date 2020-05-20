import math
def main():
    x1= int(input("Entrer la valeur de x1 = "))
    x2= int(input("Entrer la valeur de x2 = "))
    y1= int(input("Entrer la valeur de y1 = "))
    y2= int(input("Entrer la valeur de y2 = "))

    distance =  math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))

    print("La distance entre A et B est: " + str(distance))

if __name__ == "__main__":
    main()