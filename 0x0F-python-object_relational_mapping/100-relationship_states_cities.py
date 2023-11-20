#!/usr/bin/python3
"""
This script prints all city Object
from the db hbtn_0e_14_usa.
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the db and get the cities
    from the db.
    """

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3])

    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    cal_state = State(name='California')
    sfr_city = City(name='san Francisco')
    cal_state.cities.append(sfr_city)

    session.add(cal_state)
    session.commit()
    session.close()
