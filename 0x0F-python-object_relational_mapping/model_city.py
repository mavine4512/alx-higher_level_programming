#!/usr/bin/python3
"""
This script defines a City class
to work with MySQLAlchemy ORM.
"""
from model_state import State, Base
from sqlalchemy import Column, Integer, String, ForeignKey

class City(Base):
    """City class
    Attributes:
        __tablename__ (str): The table name of the class
        id(int): The id of the  class
        name (str): The name of the class
        state_id (int): the state of the city
    """
    __tablename__ = 'cities'

    id = Column(Interger, primary_key=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
