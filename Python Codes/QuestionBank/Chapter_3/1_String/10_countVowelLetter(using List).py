#WAP to find the occurrence of vowel letter in a String.
str1="Hello Kritika My name is Rekha".lower()
vowel=['a','e','i','o','u']
count=0
for i in str1:
    if i in vowel:
       count+=1

print(count)