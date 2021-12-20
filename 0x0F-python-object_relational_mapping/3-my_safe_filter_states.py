#!/usr/bin/python3
""" Wait, do you remember the previous task? Did you test "Arizona';
TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '" as an input?
What? Empty?

Yes, it’s an SQL injection to delete all records of a table…
Once again, write a script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!

Your script should take 4 arguments:
mysql username, mysql password, database name and state name searched
(safe from MySQL injection).
You must use the module MySQLdb (import MySQLdb).
Your script should connect to a MySQL server running on localhost at port 3306.
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
        cur.execute("""SELECT * FROM states
                    WHERE states.name=%s
                    ORDER BY states.id""", (query,))

        rows = cur.fetchall()
        for row in rows:
            print(row)

        cur.close()
        db.close()
