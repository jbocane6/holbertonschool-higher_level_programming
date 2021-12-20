#!/usr/bin/python3
""" Script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa:
Your script should take 3 arguments: mysql username, mysql password
and database name (no argument validation needed).
You must use the module MySQLdb (import MySQLdb).
Your script should connect to a MySQL server running on localhost at port 3306.
Results must be sorted in ascending order by states.id.
Your code should not be executed when imported.
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    argc = len(argv) - 1

    if (argc == 3):
        user, password, dbname = argv[1], argv[2], argv[3]

        db = MySQLdb.connect(host="localhost", port=3306,
                             db=dbname, user=user, passwd=password)

        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE name LIKE BINARY'N%' "
                    "ORDER BY states.id")

        rows = cur.fetchall()
        for row in rows:
            print(row)

        cur.close()
        db.close()
