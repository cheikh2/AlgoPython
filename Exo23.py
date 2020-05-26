n = int(input("Entrer le nombre de mois: "))

u = 2
v = 2
w = 2
for i in range(1, n):
    w = u + v
    u = v
    v = w
print("Au bout de "+str(n)+" mois, on aura "+str(w)+" lapins")