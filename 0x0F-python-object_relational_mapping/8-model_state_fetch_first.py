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

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(usr, pswd, db), pool_pre_ping=True)
    engine.connect()
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).where(State.id == 1).first()
    if not result:
        print("Nothing")
    else:
        print("{}: {}" .format(result.id, result.name))
    session.close()
