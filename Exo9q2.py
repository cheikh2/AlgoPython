def main():
    hd= int(input("Entrer l'heure de depart = "))
    md= int(input("Entrer minutes de depart = "))
    ha= int(input("Entrer l'heure d'arrivée = "))
    ma= int(input("Entrer minutes d'arrivée = "))

    while hd > 0 or hd <  24 or md > 0 or md < 60 and ha > 0 or ha <  24 or ma > 0 or ma < 60:
        if ha <= hd:
            dha = 24 - hd + ha
	        dma = md + ma 
        
    print("la durée du vol est : "+str(dha)+" heures et "+str(dma)+" minutes ")
    
if __name__ == "__main__":
    main()

