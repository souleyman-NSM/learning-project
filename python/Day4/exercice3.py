def ajouter_cours(etudiant, cours):
    etudiant["cours"].append(cours) 

# ➡️ Dans notre exemple, etudiant["cours"] est une liste :

# ✅ .append(cours) : La méthode .append() permet d'ajouter un élément à la fin d'une liste.

# Créer un étudiant
etudiant = {               # dictionnaire etudiant
    "nom": "Alice",
    "age": 20,
    "cours": ["Math", "Python"]   #clé valeur COURS
}

print("Cours avant :", etudiant["cours"]) # ➡️ Affiche : Cours avant : ['Math', 'Python']



ajouter_cours(etudiant, "Anglais")

# 💡 Ce que ça fait :

# ➡️ Cette ligne appelle la fonction ajouter_cours(), en lui passant deux arguments :

# etudiant : Le dictionnaire de l'étudiant.

# "Anglais" : Le nouveau cours à ajouter.

print("Cours après :", etudiant["cours"])