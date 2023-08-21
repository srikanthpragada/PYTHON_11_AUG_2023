
nums = []

while True:
    n = int(input("Enter number :"))
    if n == 0:
        break

    nums.append(n)


for n in sorted(nums):
    print(n)
