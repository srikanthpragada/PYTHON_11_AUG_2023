import sqlite3
import dbutil

con = sqlite3.connect(dbutil.DBNAME)
cur = con.cursor()
id = int(input("Enter id :"))
try:
    cur.execute("delete from employees where id = ?", (id,))
    if cur.rowcount == 1:
        print("Deleted Successfully!")
        con.commit()
    else:
        print("Sorry! Employee id not found!")
except Exception as ex:
    print("Error : ", ex)

cur.close()
con.close()
