nums = [10, 20, -1, -4, 55, -22]

# Positive Numbers
for n in filter(lambda v: v > 0, nums):
    print(n)

# Even Numbers
for n in filter(lambda v: v % 2 == 0, nums):
    print(n)