class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print(" move")

    def draw(self):
        print(" draw")

point1 = Point(1, 2)
point1 = Point()
point1.x=10
point1.y=20
print(point1.x)
point1.draw()

point2 = Point()
point2.x=1
print(point2.x)

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"hello {self.name}")


john= Person("maham")
john.talk()

print(john.name)
john.talk()

#inhertance
class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    pass


class Cat(Mammal):
    def be_annoying(self):
        print("I am annoying")


cat1 = Cat()
cat1.be_annoying()

dog1 = Dog()
dog1.walk()