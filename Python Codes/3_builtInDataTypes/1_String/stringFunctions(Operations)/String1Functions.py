#calculate the length of the string
str1="hello Dipesh!!"
length=len(str1)
print(length)



print(str1.upper()) #convert the string to upper case
print(str1.lower()) #convert the string to lowe case
print(str1.swapcase()) # convert upper case to lower and lower case to upper
print(str1.rstrip("!")) # Remove unwanted characters from last
print(str1.replace("Dipesh","Kritika")) # remove old one and add new one word or character to string (replace)
print(str1.split()) #convet string to list
print(str1.capitalize()) # Convert the first letter to the capital and rest of the practise sets to the small letters
print(str1.count("e")) #It counts the letter or word how many times of repeated
print(str1.startswith("h")) #return true if it is start with the given value else return false
print(str1.endswith("!")) # return true if it is ends with the given value else return false
print(str1.find("e")) #it finds the first index of the given value else it returns -1
print(str1.index("e")) # it is similar to the find, but it doesn't throw -1 when it throws the error if the given value is not found in string if it found then it gives its first index








#note
#stirng are immutable so they can not be changed
# while using string function they are just making new string
# not edit in original string
