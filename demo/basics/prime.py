
num = 25
for i in range(2, num//2 + 1):
    if num % i == 0:
        print("Not prime")
        break
else:
    print("Prime")


prime = True
for i in range(2, num//2 + 1):
    if num % i == 0:
        print("Not prime")
        prime = False
        break

if prime:
    print("Prime")
