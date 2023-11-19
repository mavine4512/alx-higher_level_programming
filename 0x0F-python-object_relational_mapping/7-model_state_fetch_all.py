#!/usr/bin/python3
"""
This script lists all state Objects
from the db hbtn_0e_6_usa.
"""

form sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the  db and get the states
    from the db.
    """

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3])

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()
    statesa = session.query(State).order_by(State.id).all()

    for instance in statesa:
        print('{0}: {1}'.format(instance.id, instance.name))
