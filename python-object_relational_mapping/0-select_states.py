#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
It takes three arguments: MySQL username, MySQL password, and database name.
The results are sorted in ascending order by states.id.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """
    Main function that connects to the MySQL server, retrieves and displays states.
    """

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)
    """
    The MySQLdb.connect() method establishes a connection to the MySQL server.
    Arguments:
    - host: The hostname or IP address of the server (localhost)
    - port: The port number (3306 by default for MySQL)
    - user: MySQL username
    - passwd: MySQL password
    - db: Database name to connect to
    """

    cur = db.cursor()
    """
    The cursor object allows us to execute SQL queries and fetch results.
    """

    cur.execute("SELECT * FROM states ORDER BY id ASC")
    """
    Executes an SQL query to select all records from the `states` table,
    ordered by the `id` column in ascending order.
    """

    rows = cur.fetchall()
    """
    Fetches all the rows resulting from the executed query.
    """

    for row in rows:
        print(row)
    """
    Iterates through the result set and prints each row.
    """

    cur.close()
    db.close()
    """
    Closes the cursor and the database connection to free up resources.
    """
