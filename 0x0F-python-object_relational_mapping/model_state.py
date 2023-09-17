#!/usr/bin/python3
"""
Contains the class definition of a State and an instance Base
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    # Create an SQLAlchemy engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create the 'states' table in the database
    Base.metadata.create_all(engine)

