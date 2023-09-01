names = ['Java', 'Python', 'JavaScript']


def count_upper(s):
    count = 0
    for c in s:
        if c.isupper():
            count += 1

    return count


for n in map(len, names):
    print(n)

for n in map(count_upper, names):
    print(n)

for n in map(str.upper, names):
        print(n)