"""
cont...
"""
import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='dip'
)
conn=mydb.cursor()

#insert data in DB
sql="INSERT INTO std (roll,name) VALUES(%s,%s)"
value1=(1,'Ram')
value2=(2,'Shyam')
value3=(3,'Hari')

conn.execute(sql,value1)
conn.execute(sql,value2)
conn.execute(sql,value3)

mydb.commit()  #its imp for a save query and insert it into db



#note %s is not only for string
# it is a generic placeholder
#which can hold all dataTypes
#like integer,float etc