def calculer_moyenne(etudiant):
    notes = etudiant["notes"]
    moyenne = sum(notes) / len(notes)
    print("La moyenne des notes est de ", moyenne)

etudiant = {
    "nom" : "Souleyman",
    "notes" : [10, 15, 20, 14]
}

calculer_moyenne(etudiant)