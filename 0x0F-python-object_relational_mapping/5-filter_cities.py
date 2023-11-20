#!/usr/bin/python3
"""
This script take in the name of a state
as an argument and lists all cities of that
state, using the db `hbtn_0e_4_usa`.
"""

import MySQLdb as db
from sys import argv

if __name__ == '__main__':
    """
    Access to the  db and get the states
    from the db.
    """

    db_connect = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])

    with db_connect.cursor() as db_cursor:
        db_cursor.execute("""
            SELECT
                cities.id, cities.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            WHERE
                states.name LIKE BINARY %(state_name)s
            ORDER BY
                cities.id ASC
         """, {
             'state_name': argv[4]
        })
        row_selected = db_cursor.fetchall()

    if rows_selected is not none:
        print(", ".join([row[1] for row in rows_selected]))
