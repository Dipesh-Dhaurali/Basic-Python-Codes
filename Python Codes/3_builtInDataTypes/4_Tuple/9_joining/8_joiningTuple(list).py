"""
follow pdf (96)

it will efficient for long tuple or nth tuple
"""
# List of tuples
tup1 = [(1, 2), (3, 4), (5, 6)]

# Efficient way to join tuples
temp = []
for i in tup1:
    temp.extend(i)

jnt = tuple(temp)
print(jnt)  # Output: (1, 2, 3, 4, 5, 6)
