import sqlite3

with sqlite3.connect("new.db") as conn:
    cur = conn.cursor()
    cur.execute("""DROP TABLE regions""")
    cur.execute("""CREATE TABLE IF NOT EXISTS regions (
                                                        city TEXT,
                                                        region TEXT)""")
    cities = [
        ('New York City', 'Northeast'),
        ('San Francisco', 'West'),
        ('Chicago', 'Midwest'),
        ('Houston', 'South'),
        ('Phoenix', 'West'),
        ('Boston', 'Northeast'),
        ('Los Angeles', 'West'),
        ('Houston', 'South'),
        ('Philadelphia', 'Northeast'),
        ('San Antonio', 'South'),
        ('San Diego', 'West'),
        ('Dallas', 'South'),
        ('San Jose', 'West'),
        ('Jacksonville', 'South'),
        ('Indianapolis', 'Midwest'),
        ('Austin', 'South'),
        ('Detroit', 'Midwest')
    ]

    cur.executemany("""INSERT INTO regions VALUES (?, ?)""", cities)
    cur.execute("""SELECT * FROM regions ORDER BY region ASC""")
    for r in cur.fetchall():
        print(r[0], r[1])

