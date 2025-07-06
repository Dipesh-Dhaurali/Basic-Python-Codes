# Write a python program to check the number is prime or not
n = int(input("Enter any number : "))
count = 0

for i in range(2,n):
    if n % i == 0:
        count += 1

if count == 0:
    print("It is a prime number")
else:
    print("It is not prime number")
