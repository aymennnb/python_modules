def somme(numbers):
    somme = 0
    for num in numbers:
        somme += num
    return somme

def multiplicate(numbers):
    mul = 1
    for num in numbers:
        mul *= num
    return mul

numbers = [10,5,10]
print(somme(numbers))
print(multiplicate(numbers))