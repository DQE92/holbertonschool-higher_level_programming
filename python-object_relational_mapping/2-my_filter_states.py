#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
It takes four arguments: MySQL username, MySQL password, database name,
and state name searched.
The results are sorted in ascending order by states.id.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """
    Main function that connects to the MySQL server, retrieves, and displays states
    where name matches the argument.
    """

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)

    cur = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(state_name)
    cur.execute(query)
    """
    The query selects all rows from the `states` table where the name matches the user input.
    The BINARY keyword ensures case-sensitive comparison.
    The format() method inserts user input into the query.
    """

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()

