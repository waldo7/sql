# import sqlite3
import sqlite3

# connect to database
with sqlite3.connect("newnum.db") as conn:
    cur = conn.cursor()
    # while in infinite loop
    while True:
        # ask user how to proceed
        print("Enter [avg] to calculate average.")
        print("Enter [max] to get maximum number in list.")
        print("Enter [min] to get minimum number in list.")
        print("Enter [sum] to calculate sum of all the numbers.")
        print("[q] to exit.")
        selection = input("Enter your selection: ").lower()
        # if statement
        # if chose exit, exit() the program
        if selection == "q":
            print("Have a nice day!")
            exit()
        # if avg, execute sql avg function
        elif selection == "avg":
            cur.execute("""SELECT avg(numbers) FROM numbers""")
            # display result and exit loop
            print("The average is: {}".format(cur.fetchone()[0]))
        # if max, execute sql max function
        elif selection == "max":
            cur.execute("""SELECT max(numbers) FROM numbers""")
            # display result and exit loop
            print("Max number is: {}".format(cur.fetchone()[0]))
        # if min, execute sql min function
        elif selection == "min":
            cur.execute("""SELECT min(numbers) FROM numbers""")
            # display result and exit loop
            print("Min number is: {}".format(cur.fetchone()[0]))
        # if sum, execute sql sum function
        elif selection == "sum":
            cur.execute("""SELECT sum(numbers) FROM numbers""")
            # display result and exit loop
            print("Sum of total numbers is: {}".format(cur.fetchone()[0]))
        else:
            print("I don't understand your input.")

