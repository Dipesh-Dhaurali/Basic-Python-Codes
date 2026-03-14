# Armstrong number
num = 153
orgNum= num
rem = rev = arm= 0

while num!=0:
    rem = num % 10
    arm= arm+ rem ** len(str(orgNum))
    num = num // 10

if arm==orgNum:
    print("It is armstrong")
else:
    print("It is not armstrong")


#Count a digit
num=34127
count=0
while num!=0:
    num=num//10
    count=count+1
print(count)
