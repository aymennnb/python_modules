tauxe = 10
tauxd = 9

devise = str(input("Vous indiquez la devise du montant (E or $) : "))

montant = float(input("Entrer le montant DH : "))

if devise == '$':
    resultat = montant * tauxd/100
    print(f"Le nouveau montant est {resultat} $")

elif devise == 'E':
    resultat = montant * tauxe/100
    print(f"Le nouveau montant est {resultat} euro")

else:
    print("devise non connue")