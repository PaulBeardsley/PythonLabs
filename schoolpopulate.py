import sqlite3 as s

con = s.connect('store.db')
cur = con.cursor()

sql1 = 'INSERT INTO employees (fname, sname, role, salary) values(?, ?, ?, ?)'
data1 = [
    ('Martina', 'Jenkins', 'DoS', 23000),
    ('Simon', 'Jenkins', 'Teacher', 21000),
    ('Lorraine', 'Jenkins', 'Teacher', 18000),
    ('Lucy', 'Young', 'Receptionist', 16000),
    ('James', 'Sunderland', 'Teacher', 20000),
    ('Angela', 'Orosco', 'Teacher', 19000),
    ('Eddie', 'Dumbrowski', 'Teacher', 18000),
    ('Walter', 'Sullivan', 'Warden', 15000),
    ('Simon', 'Jenkins', 'Accommodation', 17000)
]

sql2 = 'INSERT INTO cars (reg, colour, make, empid) values(?, ?, ?, ?)'
data2 = [
    ('AA11777', 'Blue', 'Audi', 5),
    ('JJ66CUP', 'Silver', 'Citroen', 7),
    ('PK44TUL', 'Red', 'Mercedes', 1),
    ('QQ34BBB', 'Blue', 'Ford', 6),
    ('SA33USB', 'White', 'Seat', 8),
    ('XY21ONO', 'Blue', 'Ford', 5),
    ('ZZ9PZA', 'Red', 'Audi', 3)
]

cur.executemany(sql1, data1)
cur.executemany(sql2, data2)



con.commit()
con.close()