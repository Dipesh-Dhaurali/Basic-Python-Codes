#WAPP to reverse the number
# link https://youtu.be/aAuWRPO7KYU
num=1234

rem=rev=0

while num!=0:
    rem=num%10
    rev=rev*10+rem
    num=num//10

print(rev)

