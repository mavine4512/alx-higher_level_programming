#!/usr/bin/python3
"""
This script takes in an argument and
displays all values in the states
where `name` matches the argument
from the database `hbtn_0e_0_usa`.
This time the script is safe from
MySQL injections!
"""

import MySQLdb as db
from sys import argv

if __name__ == '__main__':
    """
    Access to the  db and get the states
    from the db.
    """
    conn = db.connect(host="localhost", port=3306,
            user=argv[1], passwd=argv[2], db=argv[3])
    db_cursor = conn.cursor()

    db_cursor.execute(
            "SELECT * FROM states WHERE name LIKE BINARY \
                    %(name)s ORDER BY id ASC", {'name': argv[4]})
    r_sel = db_cursor.fetchall()
    for row in r_sel:
        print(row)
