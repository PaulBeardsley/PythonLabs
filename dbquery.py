import sqlite3 as sl

con = sl.connect('my-test.db')

query = input("Please enter your query\n\n")

with con:
    data = con.execute(query)
    for row in data:
        print(row)
