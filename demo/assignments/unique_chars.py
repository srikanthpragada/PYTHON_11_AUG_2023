
chars = set()

while True:
    name =input("Enter name  [end to stop] :")
    if name == 'end':
        break

    chars.update(set(name))  # chars = chars | set(name)


print(chars)

