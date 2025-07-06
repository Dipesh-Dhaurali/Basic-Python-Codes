# Program to find the sum of natural numbers up to a given number using a while loop
n=int(input("Enter the nth number : "))
i=1
Sum=0
while i<=n:
    Sum=Sum+i
    i+=1
print(Sum)