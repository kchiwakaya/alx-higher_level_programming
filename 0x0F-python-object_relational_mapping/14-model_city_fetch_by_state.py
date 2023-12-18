#!/usr/bin/python3
"""script class def city
"""
from model_state import Base, State

from model_city import City

from sqlalchemy.orm import sessionmaker

from sqlalchemy import (create_engine)

import sys


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    for result in session.query(State.name, City.id, City.name)\
            .join(City, City.state_id == State.id)\
            .order_by(City.id):
        print("{}: ({}) {}".format(result[0], result[1], result[2]))
