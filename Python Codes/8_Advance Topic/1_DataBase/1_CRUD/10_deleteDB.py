"""
cont...
"""
#delete entire database
import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
)
conn=mydb.cursor()
sql="DROP Database dipesh"
conn.execute(sql)
mydb.commit()

