names = ['Bill', 'Andy Gore', 'Larry Page', 'Scott']


def has_space(s):
    return s.find(' ') >= 0


for n in filter(has_space, names):
    print(n)
