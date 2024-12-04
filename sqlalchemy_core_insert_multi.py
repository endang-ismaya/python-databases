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

# create employee list
emp_list = [
    {"name": "Aldeind", "position": "AI Engineer"},
    {"name": "Aqeela", "position": "AI Instructor Lead"},
    {"name": "Arsyila", "position": "DevOps Engineer"},
]


# insert data
# Execute and commit to db within a transaction
with engine.begin() as connection:
    result = connection.execute(employees.insert(), emp_list)
    print(result.inserted_primary_key_rows)
