class Car:

    def __init__(self, _manufacturer, __model_name):
        self._manufacturer = _manufacturer
        self.__model_name = __model_name


rx8 = Car("Mazda", "RX-8")
print(rx8._manufacturer)
