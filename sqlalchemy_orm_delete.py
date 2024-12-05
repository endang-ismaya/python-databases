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

query = session.get(Employees, 3)

if query:
    # delete
    session.delete(query)

    # commit changes
    session.commit()

# Close the session
session.close()
