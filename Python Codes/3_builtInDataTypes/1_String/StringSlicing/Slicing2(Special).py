st="MorganCollege"
#special slicing

print(st[:5]) #output(Morga)
print(st[2:]) #output(rganCollege)
print(st[:])  ##output(MorganCollege)

print(st[::]) #print all element
print(st[0::1]) # print all element
print(st[::-1]) #reverse the string
print(st[0::-1]) #it will not reverse the string
print(st[::2]) # skip 1 element


"""
Note -:


1) if the staring index is empty it means it start form 0 index

2) if the ending index is empty it means last index is (len(st)) 


3) if the both index is empty than it means that its first index is 0 
and last index is (len(st) 

 
"""
