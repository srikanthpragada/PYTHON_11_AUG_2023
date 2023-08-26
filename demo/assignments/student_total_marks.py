
data = [(3,70), (1,50), (2,60), (1,80), (3,66), (2,80), (3,55)]

students = {}

for rollno, marks in data:
    total = students.get(rollno, 0)
    students[rollno] = total + marks

for rollno, total in sorted(students.items()):
    print(rollno, total)





