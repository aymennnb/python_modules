taille = int(input("Entrer la taille du sapin : "))

for i in range(1, taille + 1):
    espaces = taille - i
    etoiles = 2 * i - 1
    print(" " * espaces + "*" * etoiles)

print(" " * (taille - 1) + "|")


