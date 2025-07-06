"""
cont...
"""
#frozen set are the immutable set so we cannot change items form here
fruits1=['apple','banana','mango','cherry']
fruits2=['mango','orange','pineapple']
set1=frozenset(fruits1)
set2=frozenset(fruits2)


#operations
 # set1.add('pineapple') # it throw the error
 # set1.remove('mango')  # it throw the error


#do_able operations are
set3=set1.union(set2)
print(set3)

set4=set1.intersection(set2)
print(set4)

set5=set1.copy()
print(set5)