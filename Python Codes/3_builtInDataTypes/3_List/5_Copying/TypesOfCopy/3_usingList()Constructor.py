"""
https://youtu.be/ZMCte_LHml0
(6:10)
"""
lst=[2,3,4,5,6]
l=list(lst)      #note:- we need to call the list constructor function {  list()  }.
l[0]=1
print("Original list : ",lst)
print("Copied list   : ",l)

# it solved the previous problem
# which means modifying to the copied list doesn't affect to the original list