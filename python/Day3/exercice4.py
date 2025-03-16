import random

def jouer():
    secret = random.randint(1, 100) 
    tentatives = 0
    trouve = False

    while not trouve:
        devine = int(input("devine quel chiffre secret :"))
        tentatives += 1

        if devine > secret:
            print("TROP GRAND !")
        
        elif devine < secret:
            print("TROP PETIT !")

        else :
            print("BRAVO MON GARS TU AS TROUVER EN", tentatives, "tentatives")
            trouve = True

while True:
    jouer()
    rejouer = input("Veux-tu rejouer ? (o/n) :")
    if rejouer.lower() != 'o':
        break