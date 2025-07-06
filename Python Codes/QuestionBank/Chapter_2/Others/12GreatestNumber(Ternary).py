# WAPP to find the greatest number among three numbers
a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
c=int(input("Enter the value of c : "))


result=a if (a>b and a>b) else (b if b>c else c)
print(result)