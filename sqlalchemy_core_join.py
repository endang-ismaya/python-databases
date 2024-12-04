import sqlalchemy as sal

# Create engine
engine = sal.create_engine("sqlite:///databases/hr.db")

# Create metadata and reflect the table
meta_data = sal.MetaData()
employees = sal.Table("Employees", meta_data, autoload_with=engine)
