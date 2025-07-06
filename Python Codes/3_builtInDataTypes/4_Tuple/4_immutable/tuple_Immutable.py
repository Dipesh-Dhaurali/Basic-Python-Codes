# tuple is immutable
# it cannot be change in runtime after creating the tuple

tup=(5,6,2,7,9,10)

tup[3]=100   # it thorows an error because it cannot be change it is immutable
print(tup)


"""
    tup[3]=100
    ~~~^^^
TypeError: 'tuple' object does not support item assignment"""