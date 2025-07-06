"""
follow pdf (77) chapter 3

Creating a New Tuple with Modified Elements using slicing

You can create a new tuple by concatenating 
slices of the original tuple 
with the new values.

"""

# Original tuple
tuple1 = (1, 2, 3, 4)

# Creating a new tuple with updated values using slicing
tuple2 = tuple1[:2] + (99,) + tuple1[2:]
print(tuple2)  # Output: (1, 2, 99, 3, 4)
