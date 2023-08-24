data = "40,50,60,abc,34"

marks = data.split(",")
#print(marks)

total = 0
for m in marks:
    if m.isdigit():
        total += int(m)

print(total)