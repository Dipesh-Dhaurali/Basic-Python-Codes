"""
https://youtu.be/-_L0SHhFMC4
Neso Academy (2_List Comprehension in Python)

"""


names=['Rita','Kritika','Rekha','Gita','Ram','Hari']

# normal way
n=[]
for i in names:

    if 'R' in i:
        n.append(i)

print(n)  #output ['Rita', 'Rekha', 'Ram']


# syntax
# list = [expression for item in iterable if condition==True]

nme=[i for i in names if 'R' in i]
print(nme)