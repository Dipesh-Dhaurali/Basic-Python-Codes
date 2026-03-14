#Reverse a String
str="Hello"
print(str[::-1])

############ looping method ##################
text = "mom"
rev = ""

for i in text:
    rev = i + rev

print(rev)

###################################Palindrome###############
s="mom"
r=s[::-1]
if s==r:
    print("It is palindrome")
else:
    print("It is not palindrome")

