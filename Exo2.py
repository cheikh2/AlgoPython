import math
perimetre = float
surface = float
Pi = 4 * math.atan(1)

rayon = float(input("Entrer le rayon du cercle = "))
perimetre=rayon * 2 * Pi
surface = (rayon * rayon) * Pi
print("Le perimetre est: " + str(perimetre))
print("La surface est: " + str(surface))
