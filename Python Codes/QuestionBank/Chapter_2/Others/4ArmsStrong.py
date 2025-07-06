#WAPP to Armstrong
# 153
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



#1634   = 1 + 1296 + 81 + 256 = 1634

