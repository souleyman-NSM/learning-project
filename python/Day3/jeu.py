
def batman():
    secret = "123456"
    devine = ""
    trouve = False

    while not trouve:
        devine = input("devine le mot de passe :")

        if devine != secret:
            print("Faux! essaye encore")
        else:
            print("BRAVO")
            trouve = True
    
while True
    batman()