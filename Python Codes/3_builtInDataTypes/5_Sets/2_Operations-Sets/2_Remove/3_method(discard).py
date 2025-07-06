"""
CWH(#32) (11:45)
"""
set1={1,2,3,4,5,6,7,8}

set1.discard(4)
print(set1)  #{1, 2, 3, 5, 6, 7, 8}
set1.discard(10)
print(set1)    # {1, 2, 3, 5, 6, 7, 8} # nothing remove and no error

#the main different between remove and discard is that
# if you delete the non-existence element form the
# set then remove method will raise error while
# discard method will not raise error
