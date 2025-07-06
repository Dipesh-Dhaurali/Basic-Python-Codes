"""
cont... (learn coding) () + cont...(mysirg #6)
"""
# Extracting values from DB using select
import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='dip'
)
conn=mydb.cursor()

#select operation
sql='SELECT * from std'
conn.execute(sql)

#to print or fetch data form db
result=conn.fetchall()
for i in result:
    print(i)