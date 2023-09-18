#!/usr/bin/python3
"""
Adds the State object “California” with the City object “San Francisco”
to a database using SQLAlchemy.
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create a connection to the database
    db_engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                              format(sys.argv[1], sys.argv[2], sys.argv[3]),
                              pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(db_engine)

    # Create all the tables in the database which are defined
    # in your Base class (Base is defined in relationship_state.py)
    Base.metadata.create_all(db_engine)

    # Create a new session
    session = Session()

    # Create a new State and City objects
    new_state = State(name="California")
    new_city = City(name="San Francisco", state=new_state)

    # Add the State and City objects to the session
    session.add(new_state)
    session.add(new_city)

    # Commit the transaction
    session.commit()

    # Close the session
    session.close()
