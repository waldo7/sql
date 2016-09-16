import sqlite3

with sqlite3.connect("new.db") as conn:
    cur = conn.cursor()
    cur.execute("""SELECT DISTINCT population.city, population.population, regions.region
                    FROM population, regions
                    WHERE population.city = regions.city
                    ORDER BY population.city ASC""")
    for r in cur.fetchall():
        print("City: {}".format(r[0]))
        print("Population {}".format(r[1]))
        print("Region: {}".format(r[2]))
        print()
