import sqlite3 as sl

con = sl.connect('my-test.db')

sql = 'INSERT INTO USER (id, name, age) values(?, ?, ?)'
data = [
    (1, 'Yvonne', 21),
    (2, 'Bob', 22),
    (3, 'Aaron', 23),
    (4, 'Daphne', 40),
    (5, 'Alice', 12),
    (6, 'Fiona', 22)
]

with con:
    con.executemany(sql, data)
