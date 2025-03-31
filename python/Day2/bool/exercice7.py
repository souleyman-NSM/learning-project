import random # la bibliothèque random

secret = random.randint(1, 100)  # génère un nombre aléatoire entre 1 et 100
tentatives = 0 #compteur à 0
trouve = False  # Variable pour savoir si l'utilisateur a trouvé

while not trouve:
    devine = int(input("Devinez le nombre entre 1 et 100 : "))
    tentatives += 1



    if devine > secret:
        print("Trop grand !")
    elif devine < secret:
        print("trop petit !")
    else :
        print("Bravo le chiffre", secret, "a été trouver en", tentatives)
        trouve = True # On sort de la boucle while