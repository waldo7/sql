import sqlite3

with sqlite3.connect("cars.db") as conn:
    cur = conn.cursor()
    cur.execute("""SELECT * FROM inventory WHERE make = "FORD" """)
    for row in cur.fetchall():
        print(row[0], row[1], row[2])
