#!/usr/bin/python3
"""
script to get all cities
"""
import MySQLdb
import sys


if __name__ == '__main__':
    args = sys.argv
    if len(args) < 4:
        exit(1)
    username = args[1]
    password = args[2]
    database = args[3]
    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=database,
                         port=3306)
    cursor = db.cursor()
    query = cursor.execute('''
        SELECT cities.id, cities.name, states.name
        FROM cities INNER JOIN states
        ON cities.state_id=states.id
        ORDER BY cities.id
        ''')
    records = cursor.fetchall()
    for row in records:
        print(row)
