"""
cont...
"""
#create a table inside DB

import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='dip'
)

conn=mydb.cursor()
#creating table
sql="CREATE TABLE std (roll INT,name VARCHAR(20))"
conn.execute(sql)
print("Table Created!!")