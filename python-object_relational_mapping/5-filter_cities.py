#! /usr/bin/pyhton3
"""
This module takes in the name of a state as an argument
and lists all 'cities' of that state,
using the database 'hbtn_0e_4_usa'
"""
import MySQLdb
import sys
__name__ == "__main__"
username = sys.argv[1]
password = sys.argv[2]
database_name = sys.argv[3]
state_name = sys.argv[4]
db = MySQLdb.connect(host="localhost", user=username,
                     passwd=password, db=database_name)
cursor = db.cursor()
query = "SELECT cities.name FROM cities \
        JOIN states ON cities.state_id = states.id \
        WHERE states.name = %s ORDER BY cities.id ASC"
cursor.execute(query, ["{}".format(state_name)])
cities = cursor.fetchall()
result = ', '.join(item[0] for item in cities)
print(result)
cursor.close()
db.close()
