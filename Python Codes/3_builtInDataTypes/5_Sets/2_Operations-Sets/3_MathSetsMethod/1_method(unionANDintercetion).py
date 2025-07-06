"""
https://youtu.be/078tYSD7K8E?list=PLGjplNEQ1it8-0CmoljS5yeV-GlKSUEt0

Shradha Khapra (Lecture 4 : 7_Dictionary & Set in Python) (39:46)
"""
#union set
# combines both set values and returns new unique values without duplicate values
set1={1,2,3,4}
set2={3,4,5,6}

finalSet=set1.union(set2)
print(finalSet)          #{1, 2, 3, 4, 5, 6}


#Intersection
#combines common values and return new
finalSet1=set1.intersection(set2)
print(finalSet1)          #{3, 4}

