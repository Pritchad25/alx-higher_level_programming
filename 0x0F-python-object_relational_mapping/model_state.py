#!/usr/bin/python3
"""This module provides the definition the State class
for SQLAlchemy."""

import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """This defines the State class to repreent the
    states table in MySQL.

    Attributes:
        id (int): the unique integer (primary key).
        name (str): the string representing the name of
        the state.
    Args:
        Base (sqlalchemy.ext.declarative.declarative_base()): the base instance.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
