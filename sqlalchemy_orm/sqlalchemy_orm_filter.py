from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import and_
from sqlalchemy import or_
from sqlalchemy import not_

engine = create_engine("sqlite:///databases/hr_orm.db")
Base = declarative_base()


class Employees(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    position = Column(String, nullable=False)


# Create tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# LIKE Operator
print("*" * 30)
f1 = session.query(Employees).filter(Employees.name.like("a%"))
for emp in f1:
    print(emp.id, emp.name, emp.position)

# IN Operator
print("*" * 30)
f2 = session.query(Employees).filter(Employees.id.in_([1, 5]))
for emp in f2:
    print(emp.id, emp.name, emp.position)

# AND Operator
print("*" * 30)
f3 = session.query(Employees).filter(
    and_(Employees.id > 1, Employees.position.like("%Developer%"))
)
for emp in f3:
    print(emp.id, emp.name, emp.position)

# OR Operator
print("*" * 30)
f4 = session.query(Employees).filter(
    or_(Employees.position.like("%analyst%"), Employees.position.like("%Developer%"))
)
for emp in f4:
    print(emp.id, emp.name, emp.position)

# NOT Operator
print("*" * 30)
f5 = session.query(Employees).filter(not_(Employees.position.like("%analyst%")))
for emp in f5:
    print(emp.id, emp.name, emp.position)

# Close the session
session.close()
