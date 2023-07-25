import sqlite3 as sl

con = sl.connect('my-test.db')

user = ("""
    CREATE TABLE USER (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    );
""")

with con:
    con.execute(user)
