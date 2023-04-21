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
    pt = 3306

    myDB = MySQLdb.connect(
            host=host,
            user=usr,
            passwd=pwd,
            database=db,
            port=pt
            )
    myDB_cursor = myDB.cursor()
    myDB_cursor.execute("""SELECT * FROM states
                        WHERE states.name LIKE BINARY 'N%'
                        ORDER BY states.id ASC""")
    result = myDB_cursor.fetchall()

    for row in result:
        print(row)

    myDB_cursor.close()
    myDB.close()


if __name__ == "__main__":
    main()
