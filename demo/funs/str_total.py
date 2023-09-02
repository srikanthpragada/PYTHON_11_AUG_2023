
data = ["10,20,30",  "1,2,3", "88,44,55,55"]


for v in data:
    parts = v.split(",")
    marks = map(int, parts)
    print(sum(marks))
