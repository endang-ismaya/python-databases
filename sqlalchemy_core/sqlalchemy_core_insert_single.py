import sqlalchemy as sal

# create engine & connection
engine = sal.create_engine("sqlite:///databases/hr.db")
# conn = engine.connect()

# create meta data and Table employees
meta_data = sal.MetaData()
employees = sal.Table(
    "Employees",
    meta_data,
    sal.Column("id", sal.Integer(), primary_key=True),
    sal.Column("name", sal.String()),
    sal.Column("position", sal.String()),
)
meta_data.create_all(engine)


# insert data
# creating query
query = employees.insert().values(name="Endang", position="Software Engineer")
# Execute and commit to db within a transaction
with engine.begin() as connection:
    result = connection.execute(query)
    print(result.inserted_primary_key)
