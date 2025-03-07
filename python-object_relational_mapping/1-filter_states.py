#!/usr/bin/python3
""" List all states with a name starting with N from the hbtn_0e_0_usa """


import sys
import MySQLdb


def list_states():

    # Retrieving arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    cursor = None
    db = None

    try:
        # Database connexion
        db = MySQLdb.connect(host="localhost", user=mysql_username,
            passwd=mysql_password, db=database_name, port=3306)

        #cursor creation
        cursor = db.cursor()

        #Execute SQL query to retrieve reports sorted by id
        cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")

        # Retrieving and displaying results
        states = cursor.fetchall()
        if states:
            for state in states:
                print(state)


    except MySQLdb.Error as e:
        print(f"SQL connection or execution error : {e}")

    finally:
        # Close to connexion
        if cursor:
            cursor.close()
        if db:
            db.close()

if __name__ == "__main__":
    list_states()
