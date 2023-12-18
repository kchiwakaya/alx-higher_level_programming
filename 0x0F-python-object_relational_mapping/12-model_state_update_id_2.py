#!/usr/bin/python3
"""
    script to changw the name of a state object from a
    database using sqlalchemy
"""
from model_state import Base, State

from sqlalchemy.orm import sessionmaker

from sqlalchemy import (create_engine)

import sys


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    
    Session = sessionmaker(bind=engine)
    
    session = Session()
    toupdate_state = session.query(State).filter(State.id == 2).one()
    toupdate_state.name = 'New Mexico'
    session.commit()
