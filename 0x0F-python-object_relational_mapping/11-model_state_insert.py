#!/usr/bin/python3
"""module will use sqlalchemy to query of database table"""

from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv

if __name__ == "__main__":
    usr = argv[1]
    pswd = argv[2]
    db = argv[3]
    inpt = "Louisiana"

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(usr, pswd, db), pool_pre_ping=True)
    engine.connect()
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = State(name=inpt)
    session.add(query)
    session.commit()

    q_qwery = session.query(State).where(State.name == inpt).first()
    print("{}" .format(q_qwery.id))

    session.close()
