import sqlite3 as s

con = s.connect('store.db')
cur = con.cursor()

emp = ("""
    CREATE TABLE employees (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        fname TEXT,
        sname TEXT,
        role TEXT,
        salary INTEGER
    );
""")

car = ("""
    CREATE TABLE cars (
        reg TEXT,
        colour TEXT,
        make TEXT,
        empid INTEGER
    );
""")

cur.execute(emp)
cur.execute(car)

con.commit()
con.close()
