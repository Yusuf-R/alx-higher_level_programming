#!/usr/bin/python3
"""prints all City objects from the database"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State, Base


if __name__ == "__main__":
    usr = argv[1]
    pswd = argv[2]
    db = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(usr, pswd, db), pool_pre_ping=True)
    engine.connect()
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).order_by(State.id).all()

    for state in query:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))
    session.commit()
    session.close()
