"""
https://youtu.be/j2G68uQtOwM?list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&t=301
CWH(#33/100) (5:40)
"""
#dictionary accessing with loops/iterations
dict1={
    'name':'Dipesh',
     'age':21,
     'address':'kathmandu',
}

#1) for loop to get keys
for key in dict1:
    print(key,end=" ")
print()
"""
output
------
name age address
"""



#2) for loop to get values
for key in dict1:
    print(dict1[key],end=" ")
print()
"""
output
------
Dipesh 21 kathmandu 
"""



#3) for loop to get key and values
for key in dict1:
    print(key,dict1[key])

"""
output
------
name Dipesh
age 21
address kathmandu
"""


#3) for loop to get key and values  (modify)
for key in dict1:
    print(f"{key}:{dict1[key]}")

"""
output
------
name:Dipesh
age:21
address:kathmandu
"""



#4) for loop to get key and values
for key , value in dict1.items():
    print(key,value)

"""
output
------
name Dipesh
age 21
address kathmandu

"""


