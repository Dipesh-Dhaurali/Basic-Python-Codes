"""
https://youtu.be/lS8JLodeIs0
Clever Programmer (Python Tricks: How to Create a String from All Elements in 2_List (Join))
"""


#Joining 2_List Elements into a String
# Inside lists Change the Character of string to sentence

list1=['Hello!','I','am','a','good','python','programmer.']
print(list1)

lst=' '.join(list1) #it converts the character list to sentence list
print(lst) #Hello! I am a good python programmer.





#advance code
#using loop
sent=''
for i in list1:
    sent=sent+i+' '
print(sent)


