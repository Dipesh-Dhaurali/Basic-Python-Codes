"""
cont.(my sirg playlist #1)
+
cont.(learncoding vid)
"""

import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
)

#to create database need cursor function
conn=mydb.cursor()

#create database
sql="CREATE DATABASE dip"
conn.execute(sql)

print("Database Created!!")
