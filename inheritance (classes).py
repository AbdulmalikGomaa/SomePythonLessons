class Animal:
    def __init(self, name, age):
        self.name = name
        self.age = age


class Cat(Animal):
    def __init__(self, name, age):
        Animal.__init__(name, age)
        self.sound = "جعان"

    def make_sound(self):
        print(self.sound)

class Dog(Animal):
    def __init__(self, name, age):
        Animal.__init__(name, age)
        self.sound = "جعان بردو"

    def make_sound(self):
        print(self.sound)

cat = Cat("خالد", 19)
dog = Dog("حمزة", 25)

cat.make_sound()
dog.make_sound()

