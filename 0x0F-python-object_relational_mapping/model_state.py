#!/usr/bin/python3
"""
This script defines a State class and
a base class to work with MySQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class

    Attributes:
        __tableName__ (str): The table name of the class
        id (int): The state id of the class
    """
    __tablename__ = 'states'

    id = Column(integer, primary_key=True)
    name = Column(String(128), nullable=False)
