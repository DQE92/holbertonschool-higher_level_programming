#!/usr/bin/python3
"""
This script lists all states with a name starting with 'N' from the database hbtn_0e_0_usa.
It takes three arguments: MySQL username, MySQL password, and database name.
The results are sorted in ascending order by states.id.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """
    Main function that connects to the MySQL server, retrieves and displays states with names starting with 'N'.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]


    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    """
    The query selects all rows from the `states` table where the name starts with 'N',
    using the BINARY keyword to ensure case sensitivity.
    """

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()

~                             
