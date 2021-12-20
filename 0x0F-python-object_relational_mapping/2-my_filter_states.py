#!/usr/bin/python3
""" Script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
Your script should take 4 arguments: mysql username, mysql password,
database name and state name searched (no argument validation needed).
You must use the module MySQLdb (import MySQLdb).
Your script should connect to a MySQL server running on localhost at port 3306.
You must use format to create the SQL query with the user input.
Results must be sorted in ascending order by states.id.
Your code should not be executed when imported.
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    argc = len(argv) - 1

    if (argc == 4):
        user, password, dbname, query = argv[1], argv[2], argv[3], argv[4]

        db = MySQLdb.connect(host="localhost", port=3306,
                             db=dbname, user=user, passwd=password)

        cur = db.cursor()
        cur.execute("SELECT * FROM states "
                    "WHERE BINARY states.name='{}' ".format(query) +
                    "ORDER BY states.id")

        rows = cur.fetchall()
        for row in rows:
            print(row)

        cur.close()
        db.close()
