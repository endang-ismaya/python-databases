import sqlalchemy as sal

# Create engine
engine = sal.create_engine("sqlite:///databases/hr.db")

# Create metadata and reflect the table
meta_data = sal.MetaData()
employees = sal.Table("Employees", meta_data, autoload_with=engine)

# Execute the query and fetch results within a connection
# select all
# with engine.connect() as conn:
#     query = employees.select()
#     result = conn.execute(query)

#     # Fetch all data
#     result_set = result.fetchall()
#     print(result_set)


# select where clause
with engine.connect() as conn:
    query1 = employees.select().where(employees.columns.position == "Software Engineer")
    result = conn.execute(query1).fetchall()
    print(result)
