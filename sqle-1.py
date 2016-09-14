import sqlite3

with sqlite3.connect("new.db") as conn:
    cur = conn.cursor()
    cur.execute("""SELECT firstname, lastname from employees""")
    rows = cur.fetchall()
    for row in rows:
        print(row[0], row[1])
