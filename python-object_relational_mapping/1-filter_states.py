#! /usr/bin/python3
"""
This module lists all `states`
with a name starting with N (upper N) from the database 'hbtn_0e_0_usa'
"""
import MySQLdb
import sys
__name__ == "__main__"
username = sys.argv[1]
password = sys.argv[2]
database_name = sys.argv[3]
database = MySQLdb.connect(host="localhost", user=username,
                           passwd=password, db=database_name)
cursor = database.cursor()
query = "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY states.id ASC"
cursor.execute(quuery)
states = cursor.fetchall()
for state in states:
    print(state)

cursor.close()
database.close()
