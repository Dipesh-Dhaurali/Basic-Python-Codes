st="MorganCollege"

print(st[0:10:2]) # it skip 1 element    #output(MraCl)
print(st[0:10:3]) # it skip 2 element    #output(MgCl)
print(st[0:10:4]) # it slip 3 element    #output(Mal)

print(st[::2]) #it skip 1 element #output(MraClee)

print(st[1:5]) #output (orga)
print(st[1:5:1]) #output (orga)
print(st[1:5:]) #output (orga)


print(st[::]) # output (MorganCollege)
print(st[0::]) # output (MorganCollege)
print(st[::1]) # output (MorganCollege)
print(st[0::1]) # output (MorganCollege)
"""
note
0) step is always use as (n-1) example : if we use step as 3 it means (3-1)=2 so every time we need to skip 2 element
1) if the step size is empty it means the step size is 1
2) step size 1 refers to the no skip any element of sting
3) step size 2 refers to the skip the 1 element of sting
4) step size 3 refers to the skip the 2 element of sting
5) if the step is -1 then it reverse the string

"""
print(st[::-1]) #print the string in reverse





