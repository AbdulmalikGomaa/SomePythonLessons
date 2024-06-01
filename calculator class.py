class Calculator:
    def __init__(self, manufacturer, model):
        self.manufacturer = manufacturer
        self.model = model

    def __str__(self):
        return f"-------------------------------{self.manufacturer} {self.model}-------------------------------"

    def addition(self, var1, var2):
        print(f"Added {var2} to {var1}, result is {var1 + var2}")

    def subtraction(self, var1, var2):
        print(f"Subtracted {var2} from {var1}, result is {var1 - var2}")

    def multiplication(self, var1, var2):
        print(f"Multiplied {var1} by {var2}, result is {var1 * var2}")

    def division(self, var1, var2):
        try:
            print(f"Divided {var1} by {var2}, result is {var1 / var2}")
        except ZeroDivisionError:
            print(f"Cannot divide {var1} by {var2}")


pyrus = Calculator("pyrus", "T694")

print(pyrus)
pyrus.addition(3141334532543, -417647681432)
pyrus.subtraction(3243254, -3)
pyrus.multiplication(4343, 90)
pyrus.division(3213, 0)
pyrus.division(321, 9845)

