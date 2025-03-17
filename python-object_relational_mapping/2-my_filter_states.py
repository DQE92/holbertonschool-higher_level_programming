#!/usr/bin/python3
""" List all states with a name starting with N from the hbtn_0e_0_usa """

import MySQLdb
import sys


def list_states():

    # Retrieving arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # Connect to the MySQL database
        db = MySQLdb.connect(host="localhost", user=mysql_username,
                        passwd=mysql_password, db=database_name, port=3306)

        cursor = db.cursor()

        # Execute SQL query
        cursor.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name))

        # Fetch all results
        results = cursor.fetchall()
        for row in results:
            print(row)

    except MySQLdb.Error as e:
        print(f"SQL connection or execution error : {e}")

    finally:
        # Close the cursor and database connection
        cursor.close()
        db.close()

if __name__ == "__main__":
    list_states()
