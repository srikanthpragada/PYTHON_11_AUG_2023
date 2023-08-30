
def smallest_factor(num):
    for n in range(2, num//2 + 1):
        if num % n == 0:
            return n

    return num 



print(smallest_factor(17))
