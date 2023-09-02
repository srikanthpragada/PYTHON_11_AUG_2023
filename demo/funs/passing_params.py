def zero(n):
    print(id(n))
    n = 0
    print(id(n))



a = 100
print(id(a))
zero(a)
print(a)


