#!/usr/bin/python3
""" Script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa.
Your script should take 4 arguments:
mysql username, mysql password, database name and state name
(SQL injection free!).
You must use the module MySQLdb (import MySQLdb).
Your script should connect to a MySQL server running on localhost at port 3306.
Results must be sorted in ascending order by cities.id.
You can use only execute() once.
The results must be displayed as they are in the example below.
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
        cur.execute("""SELECT cities.name
                    FROM cities JOIN states ON cities.state_id = states.id
                    WHERE states.name=%s ORDER by cities.id""", (query,))

        rows = cur.fetchall()
        print(", ".join(row[0] for row in rows))

        cur.close()
        db.close()
