def count_digits(st):
    count = 0
    for c in st:
        if c.isdigit():
            count += 1

    return count


print(count_digits('abc'))
print(count_digits('abc12xy33'))
