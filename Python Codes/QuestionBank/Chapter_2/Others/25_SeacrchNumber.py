"""
Write a Python program that takes a number as input
from the user and checks if it is present in a predefined list
of numbers. If the number is found in the list,
print the index at which the number is found.
If the number is not found, print a
message saying that the number is not inside the list.
"""
numb = [1, 3, 4, 5, 6, 32, 15, 2, 16, 7]
Str = int(input("Enter any number: "))

for i in numb:
    if Str in numb:
        print(f"It is inside the list: found {Str} at {numb.index(Str)}")
        break
    else:
        print("It is not inside the list: not found")
        break

