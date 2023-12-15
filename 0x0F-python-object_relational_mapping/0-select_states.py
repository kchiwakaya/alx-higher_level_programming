#!/usr/bin/python3
""" Script to print all states"""
import sys
import MySQLdb

if __name == '__main__':
    """getting an array of passed arguments"""
    args = sys.argv
    """ handle inadequate arguments"""
    if len(args) < 4:
        exit(0)
    username = args[1]
    password = args[2]
    database = args[3]

    db = MySQLdb.connect(host ='localhost',user = username,
            password = password, db = database,
            port = 3306)

    cursor = db.cursor()
    query = cursor.execute("SELECT * FROM BY states.id")
    records = cursor.fetchall()
    for row in records:
        print(row)
