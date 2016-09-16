import sqlite3

with sqlite3.connect("cars.db") as conn:
    cur = conn.cursor()
    cur.execute("""SELECT * FROM inventory""")
    for r in cur.fetchall():
        print("{} {}\n{}".format(r[0], r[1], r[2]))
        # cur.execute("SELECT count(order_date) FROM orders WHERE make=? and model=?", (r[0], r[1]))
        cur.execute("""SELECT count(model) FROM orders WHERE (make=? AND model=?)""", (r[0], r[1]))
        print(cur.fetchone()[0])