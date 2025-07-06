# Program to check whether the last digit is divisible by 3 or not
n=56
a=n%10

if a%3==0:
    print(f"The last digit {a} is divisible by 3")
else:
    print(f"The last digit is {a} not divisible by 3")

