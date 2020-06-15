
class Voiture:
    """Classe Voiture pour la creation ou modification d'une voiture """
    nombre_roues = 4 # attribut de classe -> Une voiture a forcément 4 roues
    def __init__(self, marque, modele): # Constructeur
        self.marque = marque
        self.modele = modele
        self.couleur = "blanche"

    def change_couleur(self, couleur): # Méthode d'instance
        self.couleur = couleur
        print("La couleur a changé")

    def afficher_marque_modele(self):
        return print(f"La voiture est une {self.modele} {self.marque}")

ma_voiture = Voiture("Megane", "Renault")
print(ma_voiture.couleur)
ma_voiture.change_couleur("bleue")
print(ma_voiture.couleur)
ma_voiture.afficher_marque_modele()
print(ma_voiture.nombre_roues)

