number1 = float(input("first number :"))
number2 = float(input("second number :"))

operator = input("Choisir ton symbole (+, -, *) : ")

if operator == '+':
    resultat = number1 + number2
elif operator == '-':
    resultat = number1 - number2
elif operator == '*':
    resultat = number1 * number2
elif operator == '/':
    if number2 != 0:
        resultat = number1 / number2

    else:
        resultat = "Erreur : division par zéro !"    
else:
    resultat = "Opération non reconnue !"

print("Voici le résulat :", resultat)