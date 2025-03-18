def calculer_moyenne(etudiant):
    notes = etudiant["notes"]
    moyenne = sum(notes) / len(notes)
    return moyenne

etudiant = {
    "nom": "Alice",
    "age": 20,
    "notes": [10, 15, 20]
}

moyenne = calculer_moyenne(etudiant)
print("Moyenne de", etudiant["nom"], ":", moyenne)