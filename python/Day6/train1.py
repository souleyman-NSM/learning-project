class Voiture:
    def __init__(self, marque, couleur):
        self.marque = marque
        self.couleur = couleur
        self.vitesse = 0  # Nouvel attribut


    def demarrer(self):
        print(f"La voiture {self.marque} de couleur {self.couleur} démarre.")

    def arreter(self):
        print(f"La voiture {self.marque} de couleur {self.couleur} s'arrête.")

    def accelerer(self, kmh):
        self.vitesse += kmh
        print(f"La voiture {self.marque} accélère à {self.vitesse} km/h.")
        
# Créer un objet Voiture
ma_voiture = Voiture(marque="Toyota", couleur="rouge")

# Utiliser les méthodes
ma_voiture.accelerer(50)
ma_voiture.accelerer(30)