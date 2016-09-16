import sqlite3

with sqlite3.connect("new.db") as conn:
    cur = conn.cursor()

    cur.execute("""SELECT population.city, population.population,
                    regions.region FROM population, regions
                    WHERE population.city = regions.city
                    ORDER BY population.city ASC""")

    for r in cur.fetchall():
        print(r[0], r[1], r[2])