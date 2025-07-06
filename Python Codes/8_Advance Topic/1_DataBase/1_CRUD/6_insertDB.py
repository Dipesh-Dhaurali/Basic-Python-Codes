"""
cont...
"""
#insert data in db using user input
import mysql.connector as m
mydb=m.connect(
    host="localhost",
    user='root',
    password='1234',
    database='dip'
)
conn=mydb.cursor()

sql="INSERT INTO std (roll,name) VALUES(%s,%s)"
roll=input("Enter the roll no: ")
name=input("Enter the name : ")
values=[(roll,name)]

conn.executemany(sql,values)
mydb.commit()
