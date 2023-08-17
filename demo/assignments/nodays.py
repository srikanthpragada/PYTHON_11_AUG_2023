# Take month number and display no. of days

month = int(input("Enter month :"))
if month == 2:
    year = int(input("Enter year :"))
    if year % 4 == 0:
        print(29)
    else:
        print(28)
elif month == 4 or month == 6 or month == 9 or month == 11:
    print(30)
else:
    print(31)
