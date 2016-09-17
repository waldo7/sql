import sqlite3

# connect to database
with sqlite3.connect("newnum.db") as conn:
    cur = conn.cursor()

    while True:
        print("Enter [1] to calculate average.")
        print("Enter [2] to get maximum number in list.")
        print("Enter [3] to get minimum number in list.")
        print("Enter [4] to calculate sum of all the numbers.")
        print("Enter [5] to exit.")
        selection = int(input("Enter your selection: "))

        if selection in {1, 2, 3, 4}:
            operation = {
                1: """SELECT avg(numbers) FROM numbers""",
                2: """SELECT max(numbers) FROM numbers""",
                3: """SELECT min(numbers) FROM numbers""",
                4: """SELECT sum(numbers) FROM numbers"""
            }[selection]

            cur.execute(operation)
            output = {1: "Average", 2: "Maximum", 3: "Minimum", 4: "Sum"}[selection]
            print("{}: {}".format(output, cur.fetchone()[0]))
            print()

        elif selection == 5:
            print("Have a nice day!")
            exit()
        else:
            print("I don't understand your input.")
