import zope.interface

class Interhead(zope.interface.Interface):
    name = zope.interface.Attribute("e")
    def method1(self, name):
        pass
    def method2(self):
        pass

@zope.interface.implementer(Interhead)
class Iiiii(Interhead):

    def method1(self, name):
        return name + name
    def method2(self):
        return "Oh god I hate myself so much"

obg = Iiiii()
print(Interhead.implementedBy(obg))
print(Interhead.providedBy(Iiiii))
print(Interhead.providedBy(obg))
print(list(zope.interface.implementedBy(Iiiii)))
print(list(zope.interface.providedBy(Iiiii)))
print(Interhead.isEqualOrExtendedBy(Iiiii))

print(obg.method2())

class Test(Iiiii):
    def test1():


