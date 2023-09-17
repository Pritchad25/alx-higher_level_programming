#!/usr/bin/python3
"""This module lists all states from the hbtn_0e_0_usa
database."""
import sys
import MySQLdb

if __name__ == "__main__":
    import MySQLdb
    import sys

    # The following gets the command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # The following connects to the MySQL server
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
    )

    # The code below creates a cursor object to execute queries
    cursor = db.cursor()

    # The code below prepares the SQL query with placeholders
    sql_query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    # The following executes the query with the state name as a parameter
    cursor.execute(sql_query, (state_name,))

    # The following fetches all the rows returned by the query
    rows = cursor.fetchall()

    # The code below displays the results
    for row in rows:
        print(row)

    # The code below closes the cursor and database connection
    cursor.close()
    db.close()
