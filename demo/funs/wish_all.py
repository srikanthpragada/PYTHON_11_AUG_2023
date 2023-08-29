def wish(*names, msg="Hi"):
    print(msg, end=" ")
    for n in names:
        print(n, end=' ')

    print()  # goto next line


wish("Andy", "Bill", "Gaby", msg="Hello")
wish("Dave", "Joe")
