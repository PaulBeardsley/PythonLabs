import sqlite3 as s

con = s.connect('store.db')
cur = con.cursor()

#query = "SELECT * FROM USER WHERE age <= 22"
query = input("Please enter your query\n\n")

data = cur.execute(query)

for row in data:
    print(row)

con.commit()
con.close()
