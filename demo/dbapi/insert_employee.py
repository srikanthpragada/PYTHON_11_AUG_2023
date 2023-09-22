import sqlite3
import dbutil

con = sqlite3.connect(dbutil.DBNAME)
cur = con.cursor()
name = input("Enter name :")
job = input("Enter job :")
salary = int(input("Enter salary :"))
try:
    cur.execute("insert into employees(fullname,job,salary) values(?,?,?)",
                (name, job, salary))
    print("Added Employee Successfully!")
    con.commit()  # make insertion permanent
except Exception as ex:
    print("Error : ", ex)

cur.close()
con.close()
