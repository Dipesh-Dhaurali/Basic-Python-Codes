#WAPP to check the number is palindrome or not
num=1011

rem=rev=0
temp=num
while num!=0:
    rem=num%10
    rev=rev*10+rem
    num=num//10

print(rev)

if temp==rev:
    print("It is palindrome")
else:
    print("It is not Palindrome")


