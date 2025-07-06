"""
Write a program that takes a single character as
input and checks whether it is a vowel
(a, e, i, o, u) or a consonant using a
match statement.
Assume the input is a lowercase letter.

"""
strs=input("Enter any letter : ").lower()

match strs:
    case ("a" | "e" | "i" | "o" | "u"):
        print("It is an vowel letter")

    case ("!" | "@" | "#" | "%" | "^" | "&" | "*"):
        print("It is a symbols")

    case ("0"| "1"| "2"| "3"| "4"| "5"| "6"| "7"| "8"| "9"):
        print("It is an digit ")

    case _:
        print("It is a consultant letter")

