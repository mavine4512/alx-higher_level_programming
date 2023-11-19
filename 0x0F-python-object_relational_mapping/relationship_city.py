#!/usr/bin/python3
"""
This script defines a city class
to work with MySQLAlchemy ORM.
"""

from relationship_state import Base, state
from sqlalchemy import Column, Integer String, ForeignKey

class City(Base):
    """
    City class
    Attributes:
        __tablename__ (str): The table name of class
        id(int): The id of the class
        name(str): name of class
        state_id(int): The state of the city
    """
    __tablename__ = 'cities'

    id = Column(Integer, PrimaryKey=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
