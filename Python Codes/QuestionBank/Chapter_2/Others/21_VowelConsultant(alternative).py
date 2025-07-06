strs = input("Enter any character: ").lower()

if len(strs) != 1:
    print("Please enter only a single character.")
elif strs in "aeiou":
    print("It is a vowel letter.")
elif strs.isalpha():
    print("It is a consonant letter.")
elif strs.isdigit():
    print("It is a digit.")
elif strs in "!@#%^&*":
    print("It is a symbol.")

else:
    print("Invalid input.")
