def add(n1, n2):
    return n1 + n2


def mul(n1, n2):
    return n1 * n2


def mathop(p1, p2, operation):
    print(operation(p1, p2))


mathop(10, 20, add)
mathop(10, 20, mul)

