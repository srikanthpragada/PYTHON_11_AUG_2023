class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def getage(self):
        return self.__age


p1 = Person("Larry Page", 34)
print(p1.name, p1.getage())
print(p1.__dict__)
print(p1._Person__age)



