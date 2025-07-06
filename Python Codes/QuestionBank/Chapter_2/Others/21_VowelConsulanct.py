"""
Write a program that takes a single character as
input and checks whether it is a vowel
(a, e, i, o, u) or a consonant using a
ifelse statement.
Assume the input is a lowercase letter.

"""
strs=input("Enter any letters : ").lower()
vowels = ['a', 'e', 'i', 'o', 'u']
symbols = ['@', '#', '$', '%', '^', '&', '*','!']

if strs in vowels:
    print("It is an vowel letter")

elif strs in symbols:
    print("It is Symbols")

elif strs.isdigit():
    print("It is an number")

else:
    print("It is an consultant letter")
