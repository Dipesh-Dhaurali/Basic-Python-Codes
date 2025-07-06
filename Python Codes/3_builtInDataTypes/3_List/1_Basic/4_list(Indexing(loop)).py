student=['Dipesh',98.7,21,"Kathmandu"]

#positive indexing
for i in student:
    print(i,end=" ")

print()
"""
['Dipesh',98.7,21,"Kathmandu"]
["  -4   , -3 ,-2,     -1   "]  
"""

#negative indexing
for i in range(len(student)-1,-1,-1):
    print(student[i],end=" ")

