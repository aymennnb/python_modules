import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficher(self):
        print(f"Point({self.x},{self.y})")

    def distance_origine(self):
        return math.sqrt(self.x**2 + self.y**2)

    def calculer_vecteur(self, newp):
        newx = newp.x - self.x
        newy = newp.y - self.y
        return Vecteur(newx, newy)


point1 = Point(2, 3)
point2 = Point(5, 7)

# print("#afficher les points")
# point1.afficher()
# point2.afficher()
#
# print("#afficher la distance à l'origine")
# print("Distance de p1 à l'origine :", point1.distance_origine())
# print("Distance de p2 à l'origine :", point2.distance_origine())


class Vecteur:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficher(self):
        print(f"Vecteur({self.x}, {self.y})")

    def additionner(self, vecteur):
        return Vecteur(self.x + vecteur.x, self.y + vecteur.y)

    def produit_scalaire(self, vecteur):
        return self.x * vecteur.x + self.y * vecteur.y

    def norme(self):
        return math.sqrt(self.x**2 + self.y**2)


print("#le vecteur entre p1 et p2")
vecteur1 = point1.calculer_vecteur(point2)
vecteur2 = Vecteur(1, 4)

vecteur1.afficher()
vecteur2.afficher()

print("#Additionner deux vecteurs")
vecteur3 = vecteur1.additionner(vecteur2)
print("Résultat de l'addition :")
vecteur3.afficher()

print("#Calculer le produit scalaire de deux vecteurs")

print("Produit scalaire :", vecteur1.produit_scalaire(vecteur2))

print("vecteur1 :", vecteur1.norme())
print("vecteur2 :", vecteur2.norme())