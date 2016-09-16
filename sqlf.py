import sqlite3

with sqlite3.connect("new.db") as conn:
    cur = conn.cursor()
    cur.execute("""UPDATE population SET population = 4000000 WHERE city = "New York City" """)
    cur.execute("""DELETE FROM population WHERE city="Boston" """)
    print("\nNEW DATA: \n")

    cur.execute("SELECT * FROM population")
    rows = cur.fetchall()
    for r in rows:
        print(r[0], r[1], r[2])
