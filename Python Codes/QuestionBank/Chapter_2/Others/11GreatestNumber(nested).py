# WAPP to find the greatest number among three numbers
a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
c=int(input("Enter the value of c : "))


if a>b:
    if a>c:
        print(f"The greatest number is a: {a}")
    else:
        print(f"The greatest number is c: {c}")

else:
    if b>c:
        print(f"The greatest number is b: {b}")
    else:
        print(f"The greatest number is c: {c}")