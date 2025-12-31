# class Point:
#     def __init__(self,x1,y1):
#         self.x=x1
#         self.y=y1
#
#     def deplace(self,dx,dy):
#         self.x=self.x+dx
#         self.x=self.y+dy
#
#     def Affiche(self):
#         print("P: x = ",self.x, "y = ",self.y)
#
# P1=Point(2,5)
# P1.Affiche()
# P1.deplace(2,9)
# P1.Affiche()

class Eleve:
    def __init__(self,fname,lname):
        self.nom=fname
        self.prenom=lname

    def afficher_infos(self):
        print(f"nom : {self.nom} ,prenom : {self.prenom}")


eleve = Eleve("Aymen","Nabaoui")
eleve.afficher_infos()