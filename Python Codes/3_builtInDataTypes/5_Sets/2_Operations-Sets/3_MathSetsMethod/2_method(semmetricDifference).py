#pdf (109)
"""
Contains elements in either set but not in both.
Methods: symmetric_difference() or ^
"""
# symmetric_different is opposite to the difference
# only common will be removed
set1={1,2,3,4}
set2={3,4,5,6}

set3=set1.symmetric_difference(set2)
print(set3)   #{1, 2, 5, 6}
