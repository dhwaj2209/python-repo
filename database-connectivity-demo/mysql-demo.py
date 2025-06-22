# MySql in Python - CRUD Operations

# Section: Create connection from MYSQL in Python
# This section demonstrates how to establish a connection to MySQL using two different methods.
import mysql.connector
from mysql.connector import connection
con = mysql.connector.connect(host="localhost",
                              user="user1",
                              password="@user112345")
print("Connection is created")
con.close()

con = connection.MySQLConnection(host="localhost",
                              user="user1",
                              password="@user112345")
print("Connection1 is created")
con.close()

# Section: Create new table in MYSQL database in Python
# This section demonstrates how to create a new table 'users' in the 'employee' database.
from mysql.connector import connection
dic = {
"host":"localhost",
"user":"user1",
"password":"@user112345",
"database":"employee"
}
query = """
CREATE TABLE users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100)
)
"""
try:
  with connection.MySQLConnection(**dic) as con:
    with con.cursor() as cursor:
      cursor.execute(query)
      con.commit()
except mysql.connector.Error as err:
  print("Error message:", err.msg)  # error message


# Section: Select records with WHERE and ORDER BY clause
# This section demonstrates how to select records from the 'users' table with filtering and ordering.
from mysql.connector import connection
dic = {
"host":"localhost",
"user":"user1",
"password":"@user112345",
"database":"employee"
}
query = """
select * from users where id > 2 order by name;
"""
try:
    with connection.MySQLConnection(**dic) as conn:
        cur = conn.cursor()
        cur.execute(query)
        result = cur.fetchall()
        for f in result:
            print(f)
        #conn.commit()
except mysql.connector.Error as err:
    print("Connection is not established due to some error!")

# Section: Update records on MYSQL in Python
# This section demonstrates how to update a record in the 'users' table.
from mysql.connector import connection
dic = {
"host":"localhost",
"user":"user1",
"password":"@user112345",
"database":"employee"
}
query = """
update users 
set name = 'Mike' 
where id = 1;
"""
try:
    with connection.MySQLConnection(**dic) as conn:
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()


except mysql.connector.Error as err:
    print("Connection is not established due to some error!")

# Section: Delete records from MYSQL in Python
# This section demonstrates how to delete records from the 'users' table based on conditions.
from mysql.connector import connection
dic = {
"host":"localhost",
"user":"user1",
"password":"@user112345",
"database":"employee"
}
query = """
delete from users  `
where id > 3 and name = 'Adam';
"""
try:
    with connection.MySQLConnection(**dic) as conn:
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
except mysql.connector.Error as err:
    print("Connection is not established due to some error!")


