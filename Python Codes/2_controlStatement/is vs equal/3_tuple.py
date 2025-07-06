a=(1,2,3,4,5)
b=(1,2,3,4,5)

print(a is b)   # True (because same memory location and tuple is immutable, it cannot be changed so no point to make it in different location)
print(a == b)   # True (because same data_type with value)