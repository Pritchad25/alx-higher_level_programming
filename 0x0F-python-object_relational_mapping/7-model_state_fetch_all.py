#!/usr/bin/python3
"""This module retrieves and prints all states from a
MySQL database using SQLAlchemy."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    # The following creates the SQLAlchemy engine using
    # the provided MySQL credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)

     # The following code creates a session factory
     Session = sessionmaker(bind=engine)

     # The following creates a session object
     session = Session()

     # The code below retrieves all states from the
     # database and print their IDs and names
     for state in session.query(State).order_by(State.id):
         print("{}: {}".format(state.id, state.name))

