import sqlite3

with sqlite3.connect("new.db") as conn:
    cur = conn.cursor()
    try:
        cur.execute("""INSERT INTO populations
                        VALUES ("Singapore", "SG", 1000000)""")
    except sqlite3.OperationalError as e:
        print("Oops! Something went wrong. Try again...", e.args)
