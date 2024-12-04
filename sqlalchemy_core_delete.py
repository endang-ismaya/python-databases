import sqlalchemy as sal

# Create engine
engine = sal.create_engine("sqlite:///databases/hr.db")

# Create metadata and reflect the table
meta_data = sal.MetaData()
employees = sal.Table("Employees", meta_data, autoload_with=engine)

# select where clause
with engine.begin() as conn:
    query1 = employees.delete().where(employees.columns.id == 4)
    conn.execute(query1)
