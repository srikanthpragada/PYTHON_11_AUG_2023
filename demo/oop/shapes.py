import math
from abc import abstractmethod
from abc import ABC

# Abstract class
class Shape(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


class Square(Shape):
    def __init__(self, x, y, side):
        super().__init__(x, y)
        self.side = side

    def area(self):
        return self.side * self.side


class Rect(Shape):
    def __init__(self, x, y, length, width):
        super().__init__(x, y)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


c = Circle(10, 20, 15)
print(c.area())
