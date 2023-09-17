#!/usr/bin/python3

"""This module lists all states from the hbtn_0e_0_usa
database."""

import sys
import MySQLdb

if __name__ == "__main__":

    # The following part gets MySQL credentials and search
    # name from command-line arguments
    # and connects to MySQL server
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()

    # This part executes the SQL query to retrieve states
    # with the specified name.
    c.execute("SELECT * \
            FROM `states` \
            WHERE BINARY `name` = '{}'".format(sys.argv[4]))

    # The following fetches all rows and prints the states
    [print(state) for state in c.fetchall()]
