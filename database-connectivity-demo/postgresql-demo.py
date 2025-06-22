# Postgresql in Python - CRUD Operations

import psycopg2
conn = psycopg2.connect(database="employee",
                        user="postgres",
                        password="admin",
                        host="localhost",
                        port="5432")
print("Connection established")

# Open a cursor to perform database operations
cur = conn.cursor()
cur.execute("""CREATE TABLE users(
            id SERIAL PRIMARY KEY,
            name VARCHAR (50) UNIQUE NOT NULL);
            """)


# Select All
cur.execute("""select * from users""")
result  = cur.fetchall()
for f in result:
   print(f)
   print(type(f))

# Select One
cur.execute("""select * from users where id = 1""")
result  = cur.fetchone()
print(result)
print(type(result))

# Update Operation
cur.execute("UPDATE users SET name = 'Anthony' WHERE id = 2;")

# Delete Operation
cur.execute("delete from users WHERE id = 2;")

# Make the changes to the database persistent
conn.commit()
# Close cursor and communication with the database
cur.close()
conn.close()

	

