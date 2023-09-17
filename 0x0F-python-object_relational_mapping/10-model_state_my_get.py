#!/usr/bin/python3
"""This module searches for a state in a MySQL database
using SQLAlchemy."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    # The following code creates the SQLAlchemy engine
    # using the provided MySQL credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)

    # The code below creates a session factory
    Session = sessionmaker(bind=engine)

    # The following code creates a session object
    session = Session()

    # The code below searches for the specified state
    # in the database
    found = False
    for state in session.query(State):
        if state.name == sys.argv[4]:
            print("{}".format(state.id))
            found = True
            break

    # The following code prints a message if the state
    # is not found
    if found is False:
        print("Not found")
