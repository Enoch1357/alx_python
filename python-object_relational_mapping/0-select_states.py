#! /usr/bin/python3
"""
This module lists all states in a table 'states' from the database 'hbtn_0e_0_usa'
"""
__name__ == "__main__"
import MySQLdb
import sys
username = sys.argv[1]
password = sys.argv[2]
database_name = sys.argv[3]
database = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database_name)
cursor = database.cursor()
cursor.execute("SELECT * FROM states  ORDER BY states.id ASC")

cursor.close()
database.close()