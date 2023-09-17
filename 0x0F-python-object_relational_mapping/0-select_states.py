#!/usr/bin/python3
"""This is a module that lists all states from mySQL database"""
import sys
import MySQLdb

def list_states (username, password, database):
    """ This method lists all states from the database
    hbtn_0e_0_usa.
    Args:
        username: the mysql username
        password: the mysql password
        database: the mysql database
    """

    # The following connects to the MySQL server
    db = MySQLdb.connect(host='localhost',\
            port=3306,\
            user=username,\
            passwd=password,\
            db=database)
    cursor = db.cursor()

    # The following executes the SQL query to fetch all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # The following fetches all the rows from the query result
    rows = cursor.fetchall()

    # This part below prints the results
    for row in rows:
        print(row)

    # The part below closes the database connection
    db.close()

# An example usage or use case
if __name__ == '__main__':

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
