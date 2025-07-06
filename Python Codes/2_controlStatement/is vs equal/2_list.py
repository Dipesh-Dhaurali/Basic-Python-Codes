a=[1,2,3,4,5]
b=[1,2,3,4,5]

print(a is b)   # false (because different memory location and list is mutable it can be changed so no point to make it in same location)
print(a == b)   # True (because same data_type with value)