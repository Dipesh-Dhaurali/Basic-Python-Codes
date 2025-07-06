st="MorganCollege"
#start values
print(st[0:4]) #print index no 0 to 3 #output(Morg)
print(st[:4]) #print index no 0 to 4 # note 1st index empty is referring to the staring index is 0
print(st[1:4]) #print index no 1 to 3 #output(org)
print(st[2:4]) #print index no 2 to 3 #output(rg)
print(st[3:4]) #print index no 3 to 3 #output(g)

#mid value
print(st[3:10]) #print index no 3 to 9 #output(ganColl)

#mid to end
print(st[5:13]) #print index no 5 to 12 #output(nCollege)
print(st[5:]) #print index no 5 to (len(st)) #output(nCollege)
print(st[5:len(st)]) #len(st) function goes to end to string #output(nCollege)

#start to end
print(st[0:13]) #print index no 0 to 12 #output(MorganCollege)
print(st[0:])   #print index no 0 to (len(st)) #output(MorganCollege)
print(st[0:len(st)]) #print the index no 0 to the last as len function goes up to the last #output(MorganCollege)
print(st[:]) # if the both index is empty then it means that its first index is 0 and last index is (len(st)
print(st)







"""
note
end index[:4] always end with [n-1]
so, index[1:4] always start with 1st index and end with 
[n-1]=[4-1]=3rd index
"""

