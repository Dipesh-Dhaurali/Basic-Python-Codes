# Print the longest word in the list

list1 = ["Ram", "Shyam", "Dhaurali", "Sita", "Raju", "Hari"]

#longest way
longest_word = ""
length = 0

for i in list1:
    if len(i) > length:
        length = len(i) #calculate length evey time
        longest_word = i   #find the longest word evey time

print(f"The longest word is {longest_word} with a length of {length}")




#shortest way  (worst)
# Print the longest word in the list
list1.sort(key=len,reverse=True)

lth=len(list1[0])
l_word=(list1[0])
print(f"The longest word is {l_word} with a length of {lth}")




#other method (best)
larg_word = max(list1,key=len)
leth = len(larg_word)

print(f"The longest word is {larg_word} with a length of {leth}")

