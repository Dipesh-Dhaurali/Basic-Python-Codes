"""
cont... (4:40)
+ pdf (81)
"""
#example 1 (extended unpacking)
fruits=('apple','mango','orange','banana')

a,b,*c=fruits   #unpacking
print(a,b,c)    #apple mango ['orange', 'banana']



##########
#example 2   (extended unpacking)
t = (1, 2, 3, 4, 5)

# Unpacking with *
a, b, *c = t
print(a , b , c)     #1 2 [3, 4, 5]

# Unpacking with * in the middle
a, *b, c = t
print(a , b , c)     #1 [2, 3, 4] 5
