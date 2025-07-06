#Check the string is palindrome or not

str1="mom"
rev=""

for i in str1:
    rev=i+rev

if str1==rev:
    print("IT is palindrome")
else:
    print("It is not palindrome")


