import sqlite3

with sqlite3.connect("new.db") as conn:
    cur = conn.cursor()
    cur.execute("""INSERT INTO population
                    VALUES ("Kuala Lumpur", "KL", 5000000)""")
    