"""
cont...(lean coding ) (28:25)
+
cont...(mysirg #5)
"""
import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='dip'
)
conn=mydb.cursor()

sql="INSERT INTO std (roll,name) VALUES(%s,%s)"
value=[(4,'dipesh'),(5,'kritika'),(6,'rekha')]

conn.executemany(sql,value)   #need to use executemany for multiple items insert
mydb.commit()


"""
note
1) We can pass multiple values using list and tuple
2) If we are using list to insert multiple value then
we need to use executemany function instead to execute
"""