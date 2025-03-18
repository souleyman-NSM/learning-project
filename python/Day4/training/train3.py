def ajouter_cours(etudiant, cours):
    etudiant["cours"].append(cours)

etudiant = {
    "nom": "Alice",
    "age": 20,
    "cours": ["Math", "Python"]
}

ajouter_cours(etudiant, "Anglais")
print(etudiant["cours"])  # Affiche ['Math', 'Python', 'Anglais']