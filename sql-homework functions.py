import sqlite3

with sqlite3.connect("cars.db") as conn:
    cur = conn.cursor()
    sql = {
        "Ranger": """SELECT count(order_date) FROM orders WHERE model="Ford" """,
        "City": """SELECT count(order_date) FROM orders WHERE model="City" """,
        "Focus": """SELECT count(order_date) FROM orders WHERE model="Focus" """,
        "Accord": """SELECT count(order_date) FROM orders WHERE model="Accord" """,
        "Barista": """SELECT count(order_date) FROM orders WHERE model="Barista" """,
    }
    for k, v in sql.items():
        cur.execute(v)
        print("{}: {}".format(k, cur.fetchone()[0]))
