"""
https://youtu.be/078tYSD7K8E?list=PLGjplNEQ1it8-0CmoljS5yeV-GlKSUEt0

Shradha Khapra (Lecture 4 : 7_Dictionary & Set in Python ) (32:55)
"""
# sets are mutable
# sets elements are immutable

set1={1,2,3,4}

# add method
set1.add(5)
print(set1)     #{1, 2, 3, 4, 5}

set1.add("hello") #string add valid
print(set1)      #{1, 2, 3, 4, 5, 'hello'}

set1.add((5,6))  #tuple add valid
print(set1)      #{1, 2, 3, 4, 5, 'hello', (5, 6)}

set1.add([7,8])  #list add not valid because it is mutable
print(set1)       # it throws error

