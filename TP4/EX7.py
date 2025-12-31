import random
tableau_jeu=[]

for i in range(0,10):
    tableau_jeu.append(random.randint(1,10))

print(tableau_jeu)
print("#Apres le sort")
tableau_jeu.sort()
print(tableau_jeu)
reponse = int(input("Entrer une valeur : "))

trouve = False

for i in range(len(tableau_jeu)):
    if tableau_jeu[i] == reponse:
        trouve = True
        break

if trouve:
    print("Gagné")
else:
    print("Perdu")