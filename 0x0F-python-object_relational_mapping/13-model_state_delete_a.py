#!/usr/bin/python3
"""This module deletes states containing the letter
"a" from a MySQL database using SQLAlchemy."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    # The code below creates the SQLAlchemy engine using
    # the provided MySQL credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)

    # The following creates a session factory
    Session = sessionmaker(bind=engine)
    # The following creates a session object
    session = Session()
    # The code below retrieves all states from the database
    for state in session.query(State):
        # The code below checks if the state's name contains
        # the letter "a"
        if "a" in state.name:
            # Code below deletes the state from the session
            session.delete(state)
    # code below commits the session to persist the changes
    session.commit()
