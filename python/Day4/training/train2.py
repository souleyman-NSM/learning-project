def show(etudiant):
    print("Nom :", etudiant["nom"])
    print("Âge :", etudiant["age"])
    print("Cours :", etudiant["cours"])
    print()  # Juste pour l'espace entre les affichages


# Définition des étudiants en dehors de la fonction
etudiant1 = {
    "nom": "Alice",
    "age": 20,
    "cours": ["Math", "Python"]
}

etudiant2 = {
    "nom": "Souleyman",
    "age": 23,
    "cours": ["faible", "de coeur"]
}

# Appels de la fonction avec chaque étudiant
show(etudiant1)

show(etudiant2)