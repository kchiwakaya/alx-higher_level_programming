#!/usr/bin/python3
"""
script to get cities belonging
to a certain state
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
    state_name = args[4]
    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=database,
                         port=3306)
    cursor = db.cursor()
    query = cursor.execute('''
        SELECT cities.id, cities.name, states.name
        FROM cities INNER JOIN states
        ON cities.state_id=states.id
        ORDER BY cities.id ASC
        ''')
    records = cursor.fetchall()
    cities = [row[1] for row in records if state_name == row[2]]
    num_cities = len(cities)
    for i, city in enumerate(cities):
        if i == num_cities - 1:
            print(city)
        else:
            print(city, end=", ")
