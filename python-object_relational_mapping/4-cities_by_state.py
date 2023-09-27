#! /usr/bin/pytohn3
"""
This module lists all cities from the database 'hbtn_0e_4_usa'
"""
import MySQLdb
import sys
__name__ =="__main__"
username = sys.argv[1]
password = sys.argv[2]
database_name = sys.argv[3]
db = MySQLdb.connect(host="localhost", user=username,
                     passwd=password, db=database_name)
cursor = db.cursor()
query = "SELECT cities.id, cities.name, states.name \
        FROM cities JOIN states ON cities.state_id = states.id \
        ORDER BY cities.id ASC"
cursor.execute(query)
cities = cursor.fetchall()
for city in cities:
    print(city)
cursor.close()
db.close()
