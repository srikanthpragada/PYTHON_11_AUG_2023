total = 0

for i in range(10):
    num = int(input("Enter number [0 to stop] :"))
    if num < 0:
        continue

    if num == 0:
        break

    total += num

print(total)
