#reverse a list
list1=['apple','ball','cat','dog','egg']

#using step and slicing
for i in list1[::-1]:
    print(i,end=" ")
print()


#using for loop
for i in range(len(list1)-1,-1,-1):
    print(list1[i],end=" ")
print()


#using reverse function
lst=list1.reverse()
print(list1)


