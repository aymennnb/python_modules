class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age}"

    def birthday (self):
        print('Happy birthday you were', self.age)
        self.age +=1
        print('You are now', self.age)

    def greeter(self, name, title='Dr', prompt='welcome', message='Live Long and Prosper'):
        print(f"{prompt} {title} {name} - {message}")


# person1 = Person("Aymen", 20)
# person2 = Person("Amine", 22)
#
# print("Le contenu des Instances de la Classe Person")
# print(person1.name, 'is', person1.age)
# print(person2.name, 'is', person2.age)
#
# print("Afficher en utilisant la méthode birthday()")
# person1.birthday()
# person2.birthday()
#
# person1.greeter("Aymen", "Mr", "Hello", "Have a good day!")
# person2.greeter("Amine")
#
# del person2


class Sport_car:
    def __init__(self, brand, model, color, horsepower, speed):
        self.brand = brand
        self.model = model
        self.color = color
        self.horsepower = horsepower
        self.speed = speed

    def __str__(self):
        return (f"Brand: {self.brand}, Model: {self.model}, Color: {self.color}, Horsepower: {self.horsepower} HP, Speed: {self.speed} km/h")

# car1 = Sport_car("Lamborghini", "Huracan", "Yellow", 602, 325)
# car2 = Sport_car("Porsche", "911 Turbo S", "Blue", 640, 330)
# car3 = Sport_car("Bugatti", "W16 Mistral", "Black", 1500, 420)
# car4 = Sport_car("volkswagen", "Golf 8 r Line", "White", 1000, 3408)
#
# print(car1)
# print(car2)
# print(car3)
# print(car4)


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimetre(self):
        return 2 * (self.length + self.width)

    def __str__(self):
        return (f"Rectangle (Length = {self.length}, Width = {self.width}) leur area est {self.area()} et leur perimetre est {self.perimetre()}")


rectangle1 = Rectangle(10, 5)
rectangle2 = Rectangle(7, 3)

print(rectangle1)
print(rectangle2)