class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x={self.x}, y={self.y}"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        if self.x > other.x:
            return True
        else:
            return False

    def __int__(self):
        return self.x * self.y




p1 = Point(10, 20)
p2 = Point(10, 20)
p3 = Point(20, 30)

print(p1, str(p1), p1.__str__())
print(p1 == p2)  # p1.__eq__(p2)
print(p3 > p2)  # p3.__gt__(p2)
print(p3 < p2)

points = [p1, p2, p3]
for p in sorted(points):
    print(p)

print(int(p1))
