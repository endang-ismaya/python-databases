import sqlalchemy as sal

# Create engine
engine = sal.create_engine("sqlite:///databases/hr.db")

# Create metadata and reflect the table
meta_data = sal.MetaData()
employees = sal.Table("Employees", meta_data, autoload_with=engine)

# select where clause
with engine.begin() as conn:
    query1 = (
        employees.update()
        .where(employees.columns.id == 3)
        .values(position="Graphic Designer")
    )
    conn.execute(query1)
