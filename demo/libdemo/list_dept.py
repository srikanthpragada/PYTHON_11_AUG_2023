f = open("employees.txt", "rt")
depts = {}

for line in f.readlines():
    parts = line.strip().split(",")
    if len(parts) < 2:
        continue

    dept, emp = parts
    if len(emp) == 0:
        continue

    employees = depts.get(dept, [])
    employees.append(emp)
    depts[dept] = employees

f.close()

for dept, employees in depts.items():
    print(dept, ",".join(employees))
