#Anagram Check
string1="listen"
string2="silent"

str1=sorted(string1)
str2=sorted(string2)

if str1==str2:
    print("They are Anagram")

else:
    print("They are not Anagram")