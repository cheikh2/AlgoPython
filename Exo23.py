n = int(input("Entrer le nombre de mois: "))

u = 2
v = 2
w = 2

for i in range(1, 12):
    w = u + v
    u = v
    v = w
print("Au bout d’un an, on aura "+str(w)+" lapins")