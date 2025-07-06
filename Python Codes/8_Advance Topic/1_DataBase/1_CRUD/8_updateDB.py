"""
cont...
"""
#update the DB table values
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='dip'
)
conn=mydb.cursor()
sql="UPDATE std set roll=%s WHERE roll=%s"
value=(100,1)
conn.execute(sql,value)
mydb.commit()
