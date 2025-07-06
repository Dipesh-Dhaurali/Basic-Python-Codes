"""
https://youtu.be/078tYSD7K8E?list=PLGjplNEQ1it8-0CmoljS5yeV-GlKSUEt0

Shradha Khapra (Lecture 4 : 7_Dictionary & Set in Python ) (32:55)
"""
set1={1,2,3,4,5,6,7,8}

#remove method
set1.remove(6)
print(set1)      #{1, 2, 3, 4, 5, 7, 8}

#pop method (it remove the random values from the set because set have no ordered so it have no index)
set1.pop()
print(set1)  #{2, 3, 4, 5, 7, 8}