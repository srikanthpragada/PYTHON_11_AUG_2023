# Take salary and display net salary

salary = int(input("Enter salary :"))

hra = salary * 30 // 100
da = salary * 20 // 100

net_salary = salary + hra + da

print(f"Basics      {salary:8}")
print(f"HRA         {hra:8}")
print(f"DA          {da:8}")
print(f"Net Salary  {net_salary:8}")
