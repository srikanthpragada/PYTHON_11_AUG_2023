nums = [10, 20, -1, -4, 55, -22]


def ispositive(n):
    return n > 0


def iseven(n):
    return n % 2 == 0


for n in filter(ispositive, nums):
    print(n)

for n in filter(iseven, nums):
    print(n)