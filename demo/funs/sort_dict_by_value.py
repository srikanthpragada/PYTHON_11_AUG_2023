d = {1: 'abc', 3: 'xyz', 4: 'def', 2: 'pqr'}

for t in sorted(d):
    print(t)

# Sort dict by value (2nd element of tuple)
for t in sorted(d.items(), key=lambda t: t[1]):
    print(t)
