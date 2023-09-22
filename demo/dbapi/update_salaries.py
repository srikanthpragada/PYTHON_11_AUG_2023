import sqlite3
import dbutil

con = sqlite3.connect(dbutil.DBNAME)
cur = con.cursor()
f = open('salaries.txt', 'rt')
updated = notfound = error = 0

for line in f.readlines():
    parts = line.strip().split(",")
    if len(parts) != 2:
        continue          # Ignore line

    try:
        id, salary = parts
        cur.execute("update employees set salary = ? where id = ?",
                     (salary, id))
        if cur.rowcount == 1:
            # print(f"Updated Employee {id} Successfully!")
            updated += 1
        else:
            # print(f"Employee {id} not found!")
            notfound += 1
    except Exception as ex:
        error += 1
        # print(f"Error while updating employee {id} -> {ex}")


con.commit()
f.close()
cur.close()
con.close()

print(f"Updated {updated} employees")
print(f"Not found  {notfound} employees")
print(f"Error updating  {error} employees")
