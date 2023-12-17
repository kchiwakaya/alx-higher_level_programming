#!/usr/bin/python3
"""script to get all states
from argument bt protected from
sql injection
"""
import MySQLdb
import sys


if __name__ == '__main__':
    args = sys.argv
    if len(args) < 5:
        exit(1)
    username = args[1]
    password = args[2]
    database = args[3]
    name = args[4]
    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=database,
                         port=3306)
    cursor = db.cursor()
    query = cursor.execute("SELECT * FROM states ORDER BY states.id")
    records = cursor.fetchall()
    for row in records:
        """ row[1] contains name column"""
        if (name == row[1]):
            print(row)
