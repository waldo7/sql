import sqlite3

with sqlite3.connect("cars.db") as conn:
    cur = conn.cursor()
    cur.execute("""CREATE TABLE orders (make TEXT, model TEXT, order_date TEXT)""")
    cars = [
        ("FORD", "Ranger", "2016-01-23"),
        ("FORD", "Ranger", "2016-02-05"),
        ("FORD", "Ranger", "2016-05-15"),
        ("HONDA", "City", "2016-02-20"),
        ("HONDA", "City", "2016-05-05"),
        ("HONDA", "City", "2016-05-15"),
        ("FORD", "Focus", "2016-06-01"),
        ("FORD", "Focus", "2016-06-05"),
        ("FORD", "Focus", "2016-07-30"),
        ("HONDA", "Accord", "2016-05-30"),
        ("HONDA", "Accord", "2016-07-23"),
        ("HONDA", "Accord", "2016-08-31"),
        ("FORD", "Barista", "2016-03-01"),
        ("FORD", "Barista", "2016-06-25"),
        ("FORD", "Barista", "2016-07-14")
    ]
    cur.executemany("""INSERT INTO orders VALUES (?,?,?)""", cars)
    cur.execute("""SELECT inventory.make, inventory.model, inventory.quantity, orders.order_date
                    FROM inventory, orders
                    WHERE inventory.model = orders.model""")
    for r in cur.fetchall():
        print("Make: {}\tModel: {}".format(r[0], r[1]))
        print("Quantity: {}".format(r[2]))
        print("Order Dates: {}".format(r[3]))
        print()
