import sqlite3

with sqlite3.connect("cars.db") as conn:
    cur = conn.cursor()
    cur.execute("""UPDATE inventory SET quantity = 5 WHERE model = "Ranger" """)
    cur.execute("""UPDATE inventory SET quantity = 34 WHERE model = "Focus" """)