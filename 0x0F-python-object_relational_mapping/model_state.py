#!/usr/bin/python3
"""
This module contains the base defination for using
sqlalchemy
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

usr = argv[1]
pswd = argv[2]
db = argv[3]
host = "localhost"
pt = 3306

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://usr:pswd@host:pt/db')
    engine.connect()

    class State(Base):
        __tablename__ = 'states'
        id = Column(Integer, primary_key=True,
                    autoincrement=True, nullable=False, unique=True)
        name = Column(String(128), nullable=False)

    Base.metadata.create_all(engine)
