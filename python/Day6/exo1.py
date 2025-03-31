class Animal:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def parler(self):
        pass  # À implémenter dans les classes enfants

class Chien(Animal):
    def parler(self):
        print(f"{self.nom} dit : Woof Woof !")

# Créer un objet Chien
mon_chien = Chien(nom="Médor", age=3)
print(f"{mon_chien.nom} a {mon_chien.age} ans.")
mon_chien.parler()