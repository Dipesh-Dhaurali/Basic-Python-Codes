"""
If you know the structure of the tuple and the
specific elements you want to change, you
can use unpacking and repacking.

pdf (79)
"""
#Update the tuple using unpacking and repacking
tuple1 = (1, 2, 3, 4)

a, b, c, d = tuple1    #unpacking
c=99                   #modify

tuple2 = (a, b, c, d)    #repacking
print(tuple2)  # Output: (1, 2, 99, 4)


"""
with out repacking updating not possible
"""