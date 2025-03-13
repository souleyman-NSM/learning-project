number1 = input("Entrez un premier nombre : ")
number2 = input("Entrez un deuxième nombre : ")

number1 = float(number1)
number2 = float(number2)

operation = input ("Choisissez une opération (+, -, *, /) :")

if operation == '+':
    resultat = number1 + number2
elif operation == '-':
    resultat = number1 - number2
elif operation == '*':
    resultat = number1 * number2
elif operation == '/':
    resultat = number1 / number2
    if number2 != 0:
        resultat = number1 / number2
    else:
        resultat = "Erreur : division par zéro"
else:
    resultat = "Opération non reconnue !" 

print("Le résultat est :", resultat)