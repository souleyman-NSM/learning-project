def rechercher_etudiant(etudiants, nom):
    for etudiant in etudiants:
        if etudiant["nom"] == nom:
            print("Nom :", etudiant["nom"])
            print("Âge :", etudiant["age"])
            print("Cours :", etudiant["cours"])
            return
    print("Aucun étudiant trouvé avec le nom :", nom)

# Créer une liste d'étudiants
etudiants = [
    {"nom": "Alice", "age": 20, "cours": ["Math", "Python"]},
    {"nom": "Bob", "age": 22, "cours": ["Physique", "Chimie"]}
]

# Appeler la fonction
rechercher_etudiant(etudiants, "Alice") , 