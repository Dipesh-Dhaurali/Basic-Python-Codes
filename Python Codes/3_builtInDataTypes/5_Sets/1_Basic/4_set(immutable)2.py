# set elements are immutable so it cannot be changed the elements but
# set are mutable so we can change sets

set1={1,2,3,4,5}

set1[0]=100
print(set1)

#it gives us error
"""
    set1[0]=100
    ~~~~^^^
TypeError: 'set' object does not support item assignment
"""