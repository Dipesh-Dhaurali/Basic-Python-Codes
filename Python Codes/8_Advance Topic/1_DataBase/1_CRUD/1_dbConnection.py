"""
https://youtu.be/57HpogJv9ZQ?list=PL7ersPsTyYt2ovOENiCfuId8vuU3P-ngT
MySirg.com(Python-MySQL playlist #1)


+

https://youtu.be/DVtS-z9U5qk
learnn coding(Python-MySQL Database Connectivity ) (8:47)
"""

import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    #database='dipesh'
)
print(mydb,"Connection Established")
print(mydb.connection_id) #15
