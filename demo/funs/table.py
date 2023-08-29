def table(num, len=10):
    for i in range(1, len + 1):
        print(f"{num:3} * {i:2} = {i * num:5}")


num = int(input("Enter number :"))
table(num, 5)

table(20, 20)
