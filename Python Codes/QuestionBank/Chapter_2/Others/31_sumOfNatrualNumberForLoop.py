# Program to find the sum of natural numbers up to a given number using a for loop
n=int(input("Enter the (n+1)th number : "))
Sum=0
for i in range(1,n):
    Sum+=i
    i+=1
print(Sum)