class A:
    def __init__(self, p1):
        self.p1 = p1


class B:
    def __init__(self, p2):
        self.p2 = p2


class C(A, B):
    def __init__(self, p1, p2):
        A.__init__(self, p1)
        B.__init__(self, p2)


obj = C(10, 20)
print(obj.p1, obj.p2)
