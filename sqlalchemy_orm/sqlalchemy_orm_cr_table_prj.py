from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine("sqlite:///databases/hr_orm.db")
Base = declarative_base()


class Employees(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    position = Column(String, nullable=False)


class Projects(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    emp_id = Column(Integer, ForeignKey("employees.id"))
    name = Column(String, nullable=False)
    employees = relationship("Employees", back_populates="projects")


Employees.projects = relationship("Projects", back_populates="employees")

# Create tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Create projects
project_data = [
    Projects(name="Rogers-Canada"),
    Projects(name="Vodafone-Germany"),
    Projects(name="ATT-US"),
]
session.add_all(project_data)

# Add and commit the change
session.commit()

# Close the session
session.close()