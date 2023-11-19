#!/usr/bin/python3
"""
This script defines a State class and
a Base class to work with MySQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import retationship
from sqlalchemy.exit.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class
    Attributes:
        __tablename__ (str): The table name of the class
        id (int): The state id of the class
        name(str): The State name of the class
        cities (:obj: `City`): the cities belong to state
    """
    __tablename__ = 'states'

    id = Column(Interger, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
