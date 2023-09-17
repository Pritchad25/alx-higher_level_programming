#!/usr/bin/python3
"""This module updates the name of a state in a
MySQL database using SQLAlchemy."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    # The following method creates the SQLAlchemy engine
    # using the provided MySQL credentials.
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)
    # The following method creates a session factory
    Session = sessionmaker(bind=engine)
    # Create a session object
    session = Session()

    # The following retrieves the state with ID 2 from the
    # database
    state = session.query(State).filter_by(id=2).first()
    # The following updates the name of the state to "New Mexico"
    state.name = "New Mexico"
    # The following commits the session to persist the changes
    session.commit()
