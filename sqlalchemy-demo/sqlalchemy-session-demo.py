# SQLAlChemy - Session in Python
from sqlalchemy import Column, Integer, String, create_engine, select, text, desc, delete
from sqlalchemy.orm import declarative_base, sessionmaker
from urllib.parse import quote_plus

Base = declarative_base()

class Orders(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    order_no = Column(String(10))
    amount = Column(Integer)

engine = create_engine(
    f"mysql+pymysql://user1:"
    f"{quote_plus("@user112345")}"
    f"@localhost:3306/employee")

Base.metadata.create_all(engine)

def get_rows():
    statement = select(Orders)
    result = session.scalars(statement).all()
    for row in result:
        print(f"Id:{row.id},"
              f"OrderNo:{row.order_no},"
              f"Amount:{ row.amount}")

def getRow(id:int):
    return session.get(Orders, id)

Session = sessionmaker(bind=engine)
with Session() as session:
    delete_query = delete(Orders).where(Orders.id.in_([1, 3]))
    session.execute(delete_query)
    session.commit()
    get_rows()







