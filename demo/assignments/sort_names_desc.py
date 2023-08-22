
names = []

while True:
    name =input("Enter name  [end to stop] :")
    if name == 'end':
        break

    names.append(name)


names.sort()
names.reverse()

for n in names:
    print(n)

