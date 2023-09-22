# Display count of employees and average salary

import sqlite3
import dbutil

try:
    con = sqlite3.connect(dbutil.DBNAME)
    cur = con.cursor()
    cur.execute("select count(id), avg(salary) from employees")  # SQL Command
    count, avg = cur.fetchone()
    print(f"Count   : {count:10}")
    print(f"Average : {avg:10.0f}")
    cur.close()
    con.close()
except Exception as ex:
    print('Error :', ex)
