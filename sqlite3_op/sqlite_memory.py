import sqlite3

# persist to disk
# conn = sqlite3.connect("databases/fisrt.db")

# temporary
conn = sqlite3.connect(":memory:")

cur = conn.cursor()

cur.execute("""
    CREATE TABLE ice_cream_flavors (
        id INTEGER PRIMARY_KEY,
        flavor TEXT,
        rating INTEGER,    
    );
""")
