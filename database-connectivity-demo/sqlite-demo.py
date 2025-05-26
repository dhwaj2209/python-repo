# SQLite3 in Python - CRUD Operations
import sqlite3
con = sqlite3.connect("shopping_cart.db")

cur = con.cursor()
c = con.execute("select * from users")
result = c.fetchall()
print(result)
for f in result:
   print("ID=", f[0])
   print("Name=", f[1])

con.close()
