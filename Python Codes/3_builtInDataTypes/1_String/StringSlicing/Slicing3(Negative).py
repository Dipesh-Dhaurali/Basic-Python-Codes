st="Apple"

"""
Here is works like this

str="  A  p  p  l  e"
str=" -5 -4 -3 -2 -1"
"""

print(st[-5:-3]) #output(Ap)
print(st[-5:-1]) #output(Appl)
print(st[-5:-2]) #output(App)

print(st[-4:-2]) #output(pp)

print(st[:-1])  #output(Appl)
print(st[-5:])  #output (Apple)

# print(st[-1:-5])     # note this is incorrect because smaller value is in starting
"""
Note
0) negative slicing always works on reverse
1) last slicing value always works on (n-1)
2) -1 is the last value 
3) if the 1st index is empty then its refer to the 0 index
4) if the last index is empty then its refer to the (len(st))
5) formula (len(st))-negativeIndex=PositiveIndex
so         5-3=2

"""