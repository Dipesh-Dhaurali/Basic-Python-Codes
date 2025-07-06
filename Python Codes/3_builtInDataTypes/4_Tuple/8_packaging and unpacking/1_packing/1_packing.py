"""
https://youtu.be/v2GmF0F7ZcA
Andy Tech Show (tuple packing and unpacking in python)
"""
a=2
b=3
c=4

t=a,b,c    #tuple packing
print(t)    #(2, 3, 4)
print(type(t)) #<class 'tuple'>

e,f,g=t   #unpacking
print(e,f,g)   # 2 3 4
