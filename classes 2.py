class Country:
    def __init__(self, name, continent):
        self.name = name
        self.continent = continent

class Egypt(Country):

    def language(self):
        print("Arabic")

    def capital(self):
        print("Cairo")

class China(Country):

    def language(self):
        print("Chinese")

    def capital(self):
        print("معرفش")


