"""
code with harry (Finally keyword in Python)
"""
lst=[1,2,3,4,5]

try:
    n=int(input("Enter the index: "))
    print(lst[n])

except IndexError as e:
    print("Index out of bound ",e)

finally:
    print("Exit..")