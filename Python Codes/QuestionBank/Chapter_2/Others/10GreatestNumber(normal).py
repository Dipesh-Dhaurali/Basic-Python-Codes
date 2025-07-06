# WAPP to find the greatest number among three numbers
a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
c=int(input("Enter the value of c : "))


if a>b and a>c:
    print(f"The greatest number is a: {a}")
elif b>c:
    print(f"The greatest number is b: {b}")
else:
    print(f"The greatest number is c: {c}")