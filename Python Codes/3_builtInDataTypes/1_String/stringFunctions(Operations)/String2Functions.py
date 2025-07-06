str1="Dipesh"
print(str1.isalnum()) #return true if it is an alphanumeric else false

"""
# alpha numeric refers to the mixed words of number[0-9] 
alphabet[a-z][A-Z] 
"""



print(str1.isalpha()) #return true if it is an alphabet else false

"""
alpha refers to only for alphabet[A-Z][a-z]
"""

print(str1.isdigit()) #return true if it is a digit numer else false (note all string should be digit )
print(str1.isnumeric()) #similar to the digit
print(str1.islower()) #return true if all the string letter are in lower case otherwise return false
print(str1.isupper()) #return true if all the string letter are in upper case otherwise return false