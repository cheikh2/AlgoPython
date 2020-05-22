rep = 1
croissant = 0
decroissant = 0
t = 1
p = 0

while rep == 1:
    n = int(input("Entrer une valeur: "))
    if n >= p:
        p  = n
        croissant  = croissant+1
    if n < p:
        p = n
        decroissant= decroissant + 1
    rep = int(input("taper 1 si vous voulez continuer à saisir: "))
    t = t+1
if t == croissant:
    print("les valeurs saisies sont dans l'ordre croissant")
elif t == decroissant:
    print("les valeurs saisies sont dans l'ordre décroissant")
else:
    print("les valeurs saisies sont dans l'ordre quelconque")