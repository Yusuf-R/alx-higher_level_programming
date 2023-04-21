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

    mysql = MySQLdb.connect(
            host=host,
            user=usr,
            pasword=pwd,
            database=db,
            port=pt
            )
    db_cursor = mysql.cursor()
    db_cursor.execute("SELECT * FROM states ORDER BY id ASC")
    result = db_cursor.fetchall()

    for row in result:
        print(row)

    db_cursor.close()
    mysql.close()


if __name__ == "__main__":
    main()
