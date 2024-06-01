from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def calc_area(self):
        pass

class Square(Shape):
    def __init__(self, sidelength):
        self.sidelength = sidelength

    def calc_area(self):
        return self.sidelength ** 2

square = Square(16)
print(square.calc_area())

