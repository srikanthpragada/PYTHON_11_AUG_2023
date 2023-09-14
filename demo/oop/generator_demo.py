def numbers():
    for i in range(1, 5):
        yield i


g = numbers()
print(type(g))

print(next(g))
print(next(g))

