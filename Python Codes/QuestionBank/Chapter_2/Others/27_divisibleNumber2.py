# Program to check whether a number is divisible by userNumber or not
n=int(input("Enter the Dividend value (n) : "))
a=int(input("Enter the Divisor  number (a) : "))


if n%a==0:
    print(f"{n} is divisible by the  {a} ")
else:
    print(f"{n} is not divisible by the  {a}")
