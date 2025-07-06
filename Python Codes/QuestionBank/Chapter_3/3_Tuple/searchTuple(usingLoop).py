"""
•	Search for a number key in this tuple using loop.
"""


tuple1=(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
key=16
for ind in tuple1:
    if key==ind:
        print(f"Search Found at {tuple1.index(ind)}")
        break

else:
    print("Search not Found")


