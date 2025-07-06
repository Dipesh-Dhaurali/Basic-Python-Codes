"""
https://youtu.be/uhvljGKWges
Gate Smashers(2_List Comprehension)
"""

marks=[20,30,40,50,60]

#using list comprehension
add=[i+2 for i in marks]
print(add)

#noraml way
mark=[]
for i in marks:
    mark.append(i+2)
print(mark)


