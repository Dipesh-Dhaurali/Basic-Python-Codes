# Reverse a number
num=121
rem=rev=0
temp=num # it is just for palindrome extra
while num!=0:
    rem=num%10
    rev=rev*10+rem
    num=num//10

print(rev)

# palindrome or not
if temp==rev:
    print("It is palindrome")
else:
    print("It is not Palindrome")