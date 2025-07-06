"""
https://youtu.be/ijXMGpoMkhQ?list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3
telusko(Function Arguments in Python #33)
"""

# note
# python doesn't support pass by value and reference

def update(x):
    print(id(x))
    x=8
    print(id(x))
    print("Inside function x= ",x)

a=10
print(id(a))
update(a)
print("Outside function a= ",a)


