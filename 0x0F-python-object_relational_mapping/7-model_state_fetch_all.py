#!/usr/bin/python3

from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv

usr = argv[1]
pswd = argv[2]
db = argv[3]

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                       .format(usr, pswd, db), pool_pre_ping=True)
engine.connect()

Session = sessionmaker(bind=engine)
session = Session()


if __name__ == "__main__":
    result = session.query(State).order_by(State.id.asc()).all()
    for row in result:
        print("{}: {}" .format(row.id, row.name))
