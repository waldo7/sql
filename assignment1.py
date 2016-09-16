import sqlite3

with sqlite3.connect("cars.db") as conn:
    cur = conn.cursor()
    cars = [
        ("FORD", "Barista", 34),
        ("HONDA", "Accord", 4),
        ("FORD", "Focus", 5),
        ("HONDA", "City", 2),
        ("FORD", "Ranger", 1)
    ]
    cur.executemany("""INSERT INTO inventory VALUES (?, ?, ?)""", cars)
