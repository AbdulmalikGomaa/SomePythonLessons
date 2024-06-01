class Shape:

    def __init__(self):
        self.area = None

    def calc_area(self):
        print(self.area)


class Square(Shape):

    def __init__(self, sidelength):
        super().__init__()
        self.sidelength = sidelength
        self.area = sidelength ** 2


class Rectangle(Shape):

    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
        self.area = length * width


class Circle(Shape):

    def __init__(self, radius):
        super().__init__()
        from math import pi
        self.area = pi * radius ** 2


class Triangle(Shape):

    def __init__(self, base_length, height):
        super().__init__()
        self.base_length = base_length
        self.height = height
        self.area = (1/2) * base_length * height
        if self.area == int(self.area):
            self.area = int(self.area)


class Rhombus(Shape):

    def __init__(self, diag1, diag2):
        super().__init__()
        self.diag1 = diag1
        self.diag2 = diag2
        self.area = (1/2) * diag1 * diag2
        if self.area == int(self.area):
            self.area = int(self.area)


s1 = Square(22)
s1.calc_area()

r1 = Rectangle(12, 16)
r1.calc_area()

c1 = Circle(6)
c1.calc_area()

t1 = Triangle(12, 18)
t1.calc_area()

rh1 = Rhombus(14, 9)
rh1.calc_area()
