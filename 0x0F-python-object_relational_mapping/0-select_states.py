#!/usr/bin/python3
"""a script that list all states from the database hbtn_0e_0_usa"""
import MySQLdb


def main(*args):
    """a module for setting up DB connection"""
    host = 'localhost'
    usr = args[0]
    pwd = args[1]
    db = args[2]
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
