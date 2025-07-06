"""
Write a program that takes two numbers and an
operator (+, -, *, /) from the user, then performs
the corresponding arithmetic operation using a
match-case statement.
"""

a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))

s=input("Enter Operators (+, -, *, /)  :  ")

match s:
    case '+':
        add=a+b
        print(add)

    case '-':
        sub=a-b
        print(sub)

    case '*':
        mul=a*b
        print(mul)

    case '/':
        div=a/b
        print(div)

    case '**':
        pw=a**b
        print(pw)



