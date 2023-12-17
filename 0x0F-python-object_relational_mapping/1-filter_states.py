#!/usr/bin/python3
"""script to get states starting wit N
"""
import MySQLdb
import sys


if __name__ == '__main__':
    args = sys.argv
    username = args[1]
    password = args[2]
    database = args[3]
    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=database,
                         port=3306)
    cursor = db.cursor()
    query = cursor.execute('''
            SELECT * FROM states
            WHERE name LIKE 'N%'
            ORDER BY states.id
            ''')
    records = cursor.fetchall()
    for row in records:
        print(row)
