L = [0,1,2,3,4,5,6,7,8,9]

#a
print ("#a")
for i in range(len(L)):
    L[i] = L[i] + 1
print(L)

#b
print ("#b")
L.append(11)
print(L)

print ("#c")
L.extend([12,13])
print(L)

print ("#d")
#Afficher le premier élément
print(L[0])
#les deux premiers eléments, le demier élément, les deux demiers eléments.
print(L[:2])
#le demier élément
print(L[-1])
#les deux demiers eléments.
print(L[-2:])

#e
print ("#e")
pair = []
impair = []

for i in range(len(L)):
    if (L[i] % 2 == 0):
        pair.append(L[i])
    else:
        impair.append(L[i])

print(pair)
print(impair)
