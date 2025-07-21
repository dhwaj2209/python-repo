# SQLAlChemy in Python
import sqlalchemy as db
from urllib.parse import quote_plus

#pymssql
engine = db.create_engine(
    f"mysql+pymysql://user1:"
    f"{quote_plus("@user112345")}"
    f"@localhost:3306/employee",
    echo=True)

metadata = db.MetaData()
conn = engine.connect()
Student = db.Table('customers1', metadata,
              db.Column('id', db.Integer(),primary_key=True),
              db.Column('name', db.String(45), nullable=False),
              db.Column('email', db.String(45), nullable=False)
              )
metadata.create_all(engine)
#query = db.insert(Student).values(id=3, name='Matthew1', email="a@aa1.com")
#Result = conn.execute(query)
#conn.commit()
#stamement_update = Student.update().where(Student.c.id == 2).values(name='Kapoor111')
#stamement_update = db.update(Student).where(Student.c.id == 2).values(name='Kapoor111')
#stamement_delete = db.delete(Student).where(Student.c.id == 1)
#conn.execute(stamement_update)
#conn.commit()

query  = Student.select()
result = engine.connect().execute(query).fetchall()
for row in result:
    print(f"Id={row[0]}, Name={row[1]}, Email={row[2]}")


