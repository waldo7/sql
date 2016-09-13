import sqlite3
import csv

with sqlite3.connect("new.db") as conn:
    cur = conn.cursor()
    employees = csv.reader(open("employees.csv", "rU"))
    cur.execute("""CREATE TABLE employees (firstname TEXT, lastname TEXT)""")
    cur.executemany("""INSERT INTO employees VALUES (?, ?)""", employees)
