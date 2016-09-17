# import random and sqlite3 library
from random import randint
import sqlite3

# connect to database
with sqlite3.connect("newnum.db") as conn:
    cur = conn.cursor()

    cur.execute("""DROP TABLE IF EXISTS numbers""")
    # create table numbers
    cur.execute("""CREATE TABLE IF NOT EXISTS numbers (numbers INT)""")

    for i in list(range(100)):
        # generate random number
        num = randint(0, 100)
        # add to database
        cur.execute("""INSERT INTO numbers VALUES (?)""", (num,))

    cur.execute("""SELECT * FROM numbers""")
    for i in cur.fetchall():
        print(i[0])
