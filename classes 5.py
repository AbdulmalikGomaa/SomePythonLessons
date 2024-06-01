class Thing:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    def getageindays(self):
        return f"{self.name} is {self.__age * 365} days old"

y = Thing("3m 7sen", 27)
print(y.getageindays())
