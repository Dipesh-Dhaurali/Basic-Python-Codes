"""
Create a db name Employee , table named emp
with the following fields:
  -id (INT)
  -name (VARCHAR(100))
  -position (VARCHAR(100))
  -salary (FLOAT)
  -DOB (DATE)
"""
import datetime

import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234"
)
conn=mydb.cursor()

#creating database
conn.execute("CREATE DATABASE IF NOT EXISTS employee")

#use database
conn.execute("USE employee")

#create a table
conn.execute("""
        CREATE TABLE IF NOT EXISTS emp(
            id INT AUTO_INCREMENT PRIMARY KEY,
            name varchar(100),
            position varchar(100),
            salary float,
            DOB date
        )
""")


# #Insert into table
sql=("""
        INSERT INTO emp (id,name,position,salary,DOB)
        Values(%s,%s,%s,%s,%s)
""")
values=[(1,'Dipesh','Manager',80000,datetime.date(2060, 1, 11)),
        (2,'Kritika','CEO',180000,datetime.date(2060, 8, 3)),
        (3,'Dipa','Director',100000,datetime.date(2065, 7, 9))
         ]
conn.executemany(sql,values)



#Retrive table values / Select form table
conn.execute("SELECT * from emp")

result=conn.fetchall()
for i in result:
    print(i)


#Update table values
conn.execute("""
        UPDATE emp
        SET salary=salary+(salary*10/100)
        WHERE salary<100000
""")
conn.execute("""
        update emp
        set position='software developer'
        where id=1
""")


#delete table values
conn.execute("""
        delete from emp
        where name='Dipa'

""")

mydb.commit()
conn.close()