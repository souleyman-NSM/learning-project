number1 = input("Entrez un premier nombre :")
number2 = input("Entre un deuxieme nombre :")

operation = input("Choisissez une opération (+,-,*) :")

if operation == '+':
    resultat = int(number1) + int(number2) 

elif operation == '-':
    resultat = int(number1) - int(number2)

elif operation == '*':
    resultat = int(number1) * int(number2)


print("Le resulat est :" , resultat)