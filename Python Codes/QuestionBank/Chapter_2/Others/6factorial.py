#Write a program to find a factorial of number
# 3!= 3*2*1
##########################################################
#using for loop
num=5

if num<0:
    facto="error"

elif num==0 or num==1:
    facto=1

else:
    facto=1
    for i in range(1,num+1):
        facto=facto*i

print(facto)

#############################################################
#using while loop
num = 5
facto = 1

if num < 0:
    facto="It's factorial is undefined"

elif num==0 or num==1:
    facto = 1

else:
    while num>1:
        facto =facto*num
        num=num-1

print(facto)

########################################################