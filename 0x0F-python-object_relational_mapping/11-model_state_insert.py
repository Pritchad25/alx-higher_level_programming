#!/usr/bin/python3
"""This module adds a new state to a MySQL database using
 SQLAlchemy."""

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

    # The following code creates a session factory
    Session = sessionmaker(bind=engine)

    # The following code creates a session object
    session = Session()

    # The code below creates a new State object for
    # Louisiana
    louisiana = State(name="Louisiana")
    # The code below adds the new state to the session
    session.add(louisiana)
    # The code below commits the session to persist the changes
    session.commit()
    # The following code prints the ID of the newly added state
    print(louisiana.id)
