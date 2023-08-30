def isprime(num: int) -> bool:
    for n in range(2, num // 2 + 1):
        if num % n == 0:
            return False

    return True


if isprime(11):
    print("Prime")
else:
    print("Not prime")
