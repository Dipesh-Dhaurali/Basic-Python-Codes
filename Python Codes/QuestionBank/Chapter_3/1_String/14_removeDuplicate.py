# Write a Python program to remove all duplicates from a string.


str1 = "banana"
result = ""
for i in str1:
    if i not in result:
        result += i
print(result)
