# Test connection

import sqlite3
import dbutil

try:
    con = sqlite3.connect(dbutil.DBNAME)
    print("Connected Successfully!")
    con.close()
except Exception as ex:
    print('Error :', ex)

