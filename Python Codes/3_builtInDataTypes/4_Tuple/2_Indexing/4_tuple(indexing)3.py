#for looping indexing in tuple # negative indexing

#tuple in numeric data
tup1=(11,21,31,41,51)
#    (-5,-4,-3,-2,-1)
for i in range(len(tup1)-1,-1,-1):
    print(tup1[i],end=" ") # 51 41 31 21 11

print()


#tuple in string data
fruits=("apple","banana","grapes","orange","mango")
#      (  -5,      -4,      -3,     -2,      -1   )
for i in range(len(fruits)-1,-1,-1):
    print(fruits[i],end=" ") #mango orange grapes banana apple