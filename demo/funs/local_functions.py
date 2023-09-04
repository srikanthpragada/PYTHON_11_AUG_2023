a = 100  # Global variable


def f1():
    global a
    b = 200  # Enclosing
    a = 10

    # Local function
    def f2():
        c = 300  # Local variable
        nonlocal b
        b = 20

        print(a, b, c)

    f2()
    print(b)


f1()
