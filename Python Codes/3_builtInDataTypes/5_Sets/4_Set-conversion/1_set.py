#convert the set into the list
set1={1,2,3,4,5,6}

#set1[0]=100  #it throws an error because of imutabLe

#converting into the list
temp=list(set1)

#updte
temp[0]=100

#convert back to the set
set1=set(temp)
print(set1)

#output
# {2, 3, 100, 5, 4, 6}
# because it is unordered set so random value will be changed