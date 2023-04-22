#!/usr/bin/python3
"""a script that list all states from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv


def main():
    """a module for setting up DB connection"""
    host = 'localhost'
    usr = argv[1]
    pwd = argv[2]
    db = argv[3]
    state_arg = argv[4]
    pt = 3306

    myDB = MySQLdb.connect(
            host=host,
            user=usr,
            passwd=pwd,
            database=db,
            port=pt
            )
    myDB_cursor = myDB.cursor()
    myquery = ("SELECT cities.name "
               "FROM cities "
               "JOIN states "
               "ON cities.state_id = states.id "
               "WHERE states.name = %s "
               "ORDER BY cities.id ASC")
    try:
        myDB_cursor.execute(myquery, (state_arg,))
    except Exception:
        return

    result = myDB_cursor.fetchall()
    display = []
    i = -1

    for dsp in result:
        display.append(dsp[0])
    for dsp in display:
        i += 1
        if i == len(display) - 1:
            print(dsp, end="")
        else:
            print(dsp, end=", ")

    myDB_cursor.close()
    myDB.close()


if __name__ == "__main__":
    main()
