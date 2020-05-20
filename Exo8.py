import math
def main():
    a= int(input("Entrer a = "))
    b= int(input("Entrer b = "))
    c= int(input("Entrer c = "))

    delta = b*b-4*a*c
    if delta < 0:
        print("Pas de solution")

    if delta ==0:
        x=-b/2*a
        print ("X="+x)

if __name__ == "__main__":
    main()