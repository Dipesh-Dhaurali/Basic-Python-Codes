#Write a Python program to find the first non-repeating character in a string.
# Example: "swiss" → "w"
str1 = "swiss"

for i in str1:
    if str1.count(i) == 1:
        print(i)



