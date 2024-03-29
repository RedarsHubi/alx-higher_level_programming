#!/usr/bin/python3
"""Listing states module"""


import MySQLdb
import sys


def list_st(usrnm, psswrd, db_nm):
    try:
        connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=usrnm,
            passwd=psswrd,
            db=db_nm,
            charset="utf8"
        )

        cursor = connection.cursor()

        query = "SELECT cities.id, cities.name, states.name \
        FROM cities JOIN states ON cities.state_id \
        = states.id"

        cursor.execute(query)

        states = cursor.fetchall()

        for zab in states:
            print(zab)

    except MySQLdb.Error as e:
        print(f"Error: {e}")

    finally:
        if 'connection' in locals() and connection.open:
            cursor.close()
            connection.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        usrnm, psswrd, db_nm = sys.argv[1], sys.argv[2], sys.argv[3]

        list_st(usrnm, psswrd, db_nm)
