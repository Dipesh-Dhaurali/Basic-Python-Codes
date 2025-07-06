"""
cont...
"""
#delete values form DB
import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='dip'
)
conn=mydb.cursor()
sql="DELETE FROM std where roll>=5"
conn.execute(sql)
mydb.commit()

