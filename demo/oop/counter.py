class Counter:
    def __init__(self):
        self.value = 0

    def inc(self):
        self.value += 1

    def dec(self):
        self.value -= 1

    def reset(self):
        self.value = 0

    @property
    def counter(self):
        return self.value


c1 = Counter()
c1.inc()
c1.inc()
c1.dec()
print(c1.counter)

