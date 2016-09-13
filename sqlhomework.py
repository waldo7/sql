import sqlite3

conn = sqlite3.connect("cars.db")

cur = conn.cursor()

cur.execute("""CREATE TABLE inventory
                (Make TEXT, Model TEXT, Quantity INT)""")

conn.close()