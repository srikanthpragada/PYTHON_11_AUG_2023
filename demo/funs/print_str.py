def print_str(st, sep=' '):
    for c in st:
        print(f"{c}{sep}", end='')


print_str("Python")
print_str("Java", '*')
