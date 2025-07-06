# extend method to join tuple
t1=(1,2,3)
t2=('a','b','c')

#converting to the list
temp1=list(t1)
temp2=list(t2)

#using extend method
#no need extra variable because it will automatically join the right side to the left side
temp1.extend(temp2)

#converting back to the tuple
t3=tuple(temp1)

print(t3)




