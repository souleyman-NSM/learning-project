def function(etudiant):
    print("nom :", etudiant["nom"])
    print("age :", etudiant["age"])
    print("richesse :", etudiant["richesse"])


etudiant0 = {
    "nom" : "batman",
    "age" : "38",
    "richesse" : "milliardaire"
}

etudiant1 = {
    "nom" : "gitlpower",
    "age" : "24",
    "richesse" : "milliardaire"
}

# Appeler la fonction

function(etudiant1)