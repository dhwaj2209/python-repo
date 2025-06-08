# SQL Server in Python - CRUD Operations
import pyodbc
server = f"localhost\\sqlexpress"
database ="Employee"
username="sa"
password="@admin"

conn = pyodbc.connect(f"DRIVER=SQL Server;"
                      f'Server={server};'
                      f'Database={database};'
                      f'UID={username};'
                      f'PWD={password};')


# Create new table
query = """
        CREATE TABLE Users(
        ID INT PRIMARY KEY,
        Name VARCHAR(100))
        """

cursor = conn.cursor()

cursor.execute(query)
conn.commit()

# Insert new records
query = """
	          insert into users  
	          ([id], [name]) 
	          values 
	          (3, 'Michel'),
	          (4, 'Rob')
        """
cursor.execute(query)
conn.commit()

# Select all records

query = """
        SELECT * from Users
        """
cursor.execute(query)
records = cursor.fetchall()
for r in records:
    print(f"Id={r[0]}, Name={r[1]}")

# Select top 1 record
query = """
        SELECT * from Users where id = 1
        """
cursor.execute(query)
records = cursor.fetchone()
print(f"Id={records[0]}, Name={records[1]}")

# Update records

query = """
          update users  
          set name='Andrew'
          where id = 3 
        """
cursor.execute(query)
conn.commit()

# Delete records from table
query = """
 	    delete from users 
 	    where id = 1 
        """


cursor.execute(query)
conn.commit()




cursor.close()
conn.close()








