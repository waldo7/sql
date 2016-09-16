import sqlite3

with sqlite3.connect("new.db") as conn:
    cur = conn.cursor()

    sql = {
        "average": "SELECT avg(population) FROM population",
        "maximum": "SELECT max(population) FROM population",
        "minimum": "SELECT min(population) FROM population",
        "sum": "SELECT sum(population) FROM population",
        "count": "SELECT count(city) FROM population"
    }

    for k, v in sql.items():
        cur.execute(v)
        print("{}: {:,.2f}".format(k, cur.fetchone()[0]))
