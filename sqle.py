import sqlite3

with sqlite3.connect("new.db") as conn:
    cur = conn.cursor()
    for row in cur.execute("""SELECT * from employees"""):
        print(row)