#!/usr/bin/python3
"""This module lists all states from the hbtn_0e_0_usa
database."""

import sys
import MySQLdb


if __name__ == "__main__":
    # The following code gets MySQL credentials and search
    # name from command-line arguments
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    # The code below connects to MySQL server
    c = db.cursor()

    # The following part executes the SQL query to
    # retrieve all states
    c.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
            FROM `cities` as `c` \
            INNER JOIN `states` as `s` \
            ON `c`.`state_id` = `s`.`id` \
            ORDER BY `c`.`id`")

    # The following code fetchs all rows and prints the states
    [print(city) for city in c.fetchall()]
