from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

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

# retrieve all employees
query = session.query(Employees).all()
for emp in query:
    print(emp.id, emp.name, emp.position)

print("*" * 30)
# retrive single employee
emp_4: Employees = session.get(Employees, 4)
if emp_4:
    print(emp_4.id, emp_4.name, emp_4.position)

print("*" * 30)
# retrieve first employee
emp_1st: Employees = session.query(Employees).first()
if emp_1st:
    print(emp_1st.id, emp_1st.name, emp_1st.position)

print("*" * 30)
# filter
filter1 = session.query(Employees).filter(Employees.position == "Data Analyst")
for emp in filter1:
    print(emp.id, emp.name, emp.position)


# Close the session
session.close()
