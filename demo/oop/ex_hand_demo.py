data = input("Enter a number :")

try:
    num = int(data)
    print(100 // num)
except ValueError:
    print("Sorry! Invalid Number")
except ZeroDivisionError:
    print("Sorry! Zero is not valid")

print("The End")
