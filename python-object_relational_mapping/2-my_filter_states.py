#! /usr/bin/python3
"""
This module takes in an argument and displays all values in the 'states' table of 'hbtn_0e_0_usa' where name matches the argument
"""
import MySQLdb
import sys
__name__ == "__main__"
username = sys.argv[1]
password = sys. argv[2]
database_name = sys.argv[3]
state_name = sys.argv[4]
database = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database_name)
cursor = database.cursor()
cursor.execute("SELECT * FROM states WHERE name={}".format(state_name))
states = cursor.fetchall()
for state in states:
    print(state)
cursor.close()
database.close()
