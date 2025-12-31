def cube(x):
    return x ** 3

def Volume_Sphere(r):
    volume = (4 * 3.14 * cube(r)) / 3
    return volume

rayon = 3

v = Volume_Sphere(rayon)

print("Le volume de la sphère est :", v)