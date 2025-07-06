"""
pdf (103)
"""
#update method
# it adds the values randomly
# note never try tho change the element by using update method on sets because sets elements are immutable
# add multiple items we use update method

set1={1,2,3,4}
set1.update([5,6,'abc'])
print(set1)

# {1, 2, 3, 4, 5, 6 ,"abc"}